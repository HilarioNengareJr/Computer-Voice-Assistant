# Command Manual

## Overview

This manual provides a comprehensive guide to the commands that can be executed through the voice command interface. The commands allow users to manage folders, applications, and system operations seamlessly.

## Command Categories

### 1. Folder Management

- **Open Folder**
  - **Command:** `open folder <folder_name>`
  - **Description:** Opens the specified folder on the system.
  - **Example:** `open folder documents`

- **Close Folder**
  - **Command:** `close folder <folder_name>`
  - **Description:** Closes the specified folder.
  - **Example:** `close folder documents`

### 2. Application Management

- **Launch Application**
  - **Command:** `launch application <app_name>`
  - **Description:** Launches the specified application. The system will search for executable files that match parts of the app name.
  - **Example:** `launch application Google Chrome`

- **Close Application**
  - **Command:** `close application <app_name>`
  - **Description:** Closes the specified application.
  - **Example:** `close application Google Chrome`

### 3. System Operations

- **Shut Down Computer**
  - **Command:** `shut down computer`
  - **Description:** Initiates system shutdown.
  - **Example:** `shut down computer`

- **Restart Computer**
  - **Command:** `restart computer`
  - **Description:** Initiates system restart.
  - **Example:** `restart computer`

### 4. Webpage Management

- **Find Webpage**
  - **Command:** `find webpage <query>`
  - **Description:** Opens a web browser and searches for the specified query using Google.
  - **Example:** `find webpage openAI`

### Additional Notes

- Commands are case-insensitive. You can use uppercase or lowercase as preferred.
- Ensure the application and folder names are accurately specified to avoid errors.
- The system searches predefined directories for executable applications and folders.

## Error Handling

If a command fails to execute, the system will provide a feedback message indicating the issue. Common errors may include:

- Folder or application not found.
- Insufficient permissions to execute a command.
- Syntax errors in command structure.

## Examples

Here are some examples of valid commands:

```bash
open folder pictures
launch application firefox
close application vlc
shut down computer
restart computer
find webpage machine learning
