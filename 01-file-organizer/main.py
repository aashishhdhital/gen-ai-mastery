"""
📂 FILE ORGANIZER - Phase 1 Project

This program automatically organizes files in a directory by type:
- Images (.jpg, .png, .gif, etc.)
- Documents (.pdf, .docx, .txt, etc.)
- Videos (.mp4, .avi, .mkv, etc.)
- Audio (.mp3, .wav, .flac, etc.)
- Code (.py, .js, .html, .css, etc.)
- Archives (.zip, .rar, .7z, etc.)

Concepts covered:
- File system operations (os module)
- String operations (file extensions)
- Dictionary data structures
- Loops and conditionals
- Error handling

Author: Gen AI Mastery
Date: 2025
"""

import os
import shutil
from organizer import get_file_type, organize_files, display_summary


def validate_directory(path):
    """
    Validate if the given path is a valid directory
    
    Parameters:
        path (str): Directory path to validate
    
    Returns:
        bool: True if valid directory, False otherwise
    """
    if not os.path.exists(path):
        print(f"❌ Error: Directory '{path}' does not exist!")
        return False
    
    if not os.path.isdir(path):
        print(f"❌ Error: '{path}' is not a directory!")
        return False
    
    return True


def get_directory_from_user():
    """
    Get directory path from user with validation
    
    Returns:
        str: Valid directory path
    """
    while True:
        path = input("\n📁 Enter the directory path to organize: ").strip()
        
        # Handle empty input
        if not path:
            print("❌ Please enter a valid path!")
            continue
        
        # Expand home directory (~)
        path = os.path.expanduser(path)
        
        # Validate the directory
        if validate_directory(path):
            return path


def confirm_action():
    """
    Ask user to confirm before organizing files
    
    Returns:
        bool: True if user confirms, False otherwise
    """
    response = input("\n⚠️  Do you want to proceed? (yes/no): ").lower().strip()
    return response in ['yes', 'y']


def main():
    """
    Main program flow
    """
    print("\n" + "="*50)
    print("     📂 FILE ORGANIZER - Phase 1 Project")
    print("="*50)
    print("\nThis tool will automatically organize your files by type.")
    print("Files will be moved into folders like:")
    print("  • Images/")
    print("  • Documents/")
    print("  • Videos/")
    print("  • Audio/")
    print("  • Code/")
    print("  • Archives/")
    print("  • Other/")
    
    # Get directory from user
    directory = get_directory_from_user()
    
    # Count files before organizing
    files_in_dir = [f for f in os.listdir(directory) 
                    if os.path.isfile(os.path.join(directory, f))]
    
    if not files_in_dir:
        print(f"\n⚠️  No files found in '{directory}'")
        print("Nothing to organize!")
        return
    
    print(f"\n📊 Found {len(files_in_dir)} files to organize")
    print("\nFiles to be organized:")
    for file in files_in_dir[:10]:  # Show first 10
        file_type = get_file_type(file)
        print(f"  • {file} -> {file_type}/")
    
    if len(files_in_dir) > 10:
        print(f"  ... and {len(files_in_dir) - 10} more files")
    
    # Confirm action
    if not confirm_action():
        print("\n❌ Operation cancelled.")
        return
    
    # Organize files
    print(f"\n🔄 Organizing files in: {directory}")
    print("="*50)
    
    try:
        summary = organize_files(directory)
        
        print("\n" + "="*50)
        print("✅ File organization complete!")
        print("="*50)
        
        # Display summary
        display_summary(summary)
        
    except Exception as e:
        print(f"\n❌ Error during organization: {e}")
        print("\nSome files may not have been organized.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
