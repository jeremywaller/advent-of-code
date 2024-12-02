import argparse
import importlib.util
import sys
import os

def load_day_module(day):
    day_folder = str(day)
    module_path = os.path.join(day_folder, "main.py")
    
    if not os.path.exists(module_path):
        print(f"Error: Could not find main.py in day {day} folder")
        sys.exit(1)
        
    spec = importlib.util.spec_from_file_location(f"day{day}", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    parser = argparse.ArgumentParser(description='Run different day solutions for the challenge.')
    parser.add_argument('day', type=int, choices=[1, 2], 
                       help='The day number to run (1 or 2)')
    
    args = parser.parse_args()
    
    # Load and run the appropriate day's module
    day_module = load_day_module(args.day)
    day_module.main()

if __name__ == "__main__":
    main()
