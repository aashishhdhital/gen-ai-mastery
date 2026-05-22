"""
File Organizer Module

This module contains the core functions for organizing files by type.

Concepts demonstrated:
- Dictionary data structures
- String operations
- File system operations
- Error handling
"""

import os
import shutil


# Dictionary mapping file extensions to folder names
# This is the CONFIGURATION - easily extensible!
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.webp'],
    'Documents': ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.txt', '.rtf'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.webm'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.rb', '.php', '.go'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.iso', '.dmg']
}


def get_file_type(filename):
    """
    Determine the file type based on extension
    
    Parameters:
        filename (str): Name of the file
    
    Returns:
        str: Category name or 'Other' if not found
    
    Example:
        >>> get_file_type('photo.jpg')
        'Images'
        >>> get_file_type('script.py')
        'Code'
    """
    # Get the file extension
    _, extension = os.path.splitext(filename)
    extension = extension.lower()  # Convert to lowercase for case-insensitive matching
    
    # Search through categories
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    
    # If no match found, return 'Other'
    return 'Other'


def create_folders(directory, categories):
    """
    Create folders for each category in the directory
    
    Parameters:
        directory (str): Path to the directory
        categories (list): List of category names
    
    Returns:
        list: List of successfully created folders
    """
    created = []
    
    for category in categories:
        folder_path = os.path.join(directory, category)
        
        # Check if folder already exists
        if not os.path.exists(folder_path):
            try:
                os.makedirs(folder_path)
                print(f"✅ Created folder: {category}/")
                created.append(category)
            except Exception as e:
                print(f"❌ Could not create folder {category}: {e}")
        else:
            print(f"ℹ️  Folder already exists: {category}/")
            created.append(category)
    
    return created


def move_file(source, destination):
    """
    Move a file to the destination folder
    
    Parameters:
        source (str): Full path to the source file
        destination (str): Full path to destination folder
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Get the filename
        filename = os.path.basename(source)
        destination_path = os.path.join(destination, filename)
        
        # Move the file
        shutil.move(source, destination_path)
        return True
    except Exception as e:
        print(f"❌ Error moving {filename}: {e}")
        return False


def organize_files(directory):
    """
    Main function to organize all files in a directory
    
    Parameters:
        directory (str): Path to the directory to organize
    
    Returns:
        dict: Summary of organized files
    """
    # Get unique categories we'll need
    categories_to_create = set(FILE_CATEGORIES.keys())
    categories_to_create.add('Other')  # Always create 'Other' folder
    
    # Create folders
    create_folders(directory, categories_to_create)
    
    # Initialize summary
    summary = {category: [] for category in categories_to_create}
    
    # Get all files in the directory
    items = os.listdir(directory)
    
    for item in items:
        item_path = os.path.join(directory, item)
        
        # Skip if it's a directory (not a file)
        if os.path.isdir(item_path):
            continue
        
        # Determine the category
        category = get_file_type(item)
        category_path = os.path.join(directory, category)
        
        # Move the file
        if move_file(item_path, category_path):
            print(f"✅ Moved {item} -> {category}/")
            summary[category].append(item)
        else:
            summary['Other'].append(item)  # Track failed moves
    
    return summary


def display_summary(summary):
    """
    Display a summary of the organization
    
    Parameters:
        summary (dict): Dictionary with organization results
    """
    print("\n📊 ORGANIZATION SUMMARY")
    print("="*50)
    
    total_files = 0
    
    for category, files in summary.items():
        if files:  # Only show categories with files
            count = len(files)
            total_files += count
            print(f"\n📁 {category}: {count} file(s)")
            for file in files[:5]:  # Show first 5
                print(f"   • {file}")
            if len(files) > 5:
                print(f"   ... and {len(files) - 5} more")
    
    print("\n" + "="*50)
    print(f"Total files organized: {total_files}")
    print("="*50)
