import argparse
import importlib.util
import sys
import os

def load_day_module(day, is_test=False):
    day_folder = str(day)
    filename = "test.py" if is_test else "solution.py"
    module_path = os.path.join(day_folder, filename)
    
    if not os.path.exists(module_path):
        print(f"Error: Could not find {filename} in day {day} folder")
        sys.exit(1)
    
    # Add the day's directory to Python path for proper imports
    day_dir = os.path.abspath(day_folder)
    if day_dir not in sys.path:
        sys.path.insert(0, day_dir)
        
    spec = importlib.util.spec_from_file_location(f"day{day}", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    parser = argparse.ArgumentParser(description='Run different day solutions for the challenge.')
    parser.add_argument('--day', type=int, choices=range(1, 8), required=True,
                       help='The day number to run (1 - 7)')
    parser.add_argument('--test', action='store_true',
                       help='Run tests instead of the main solution')
    
    args = parser.parse_args()
    
    # Load and run the appropriate module
    day_module = load_day_module(args.day, args.test)
    day_module.main()

if __name__ == "__main__":
    main()
