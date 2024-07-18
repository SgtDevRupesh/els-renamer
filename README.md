---

# els-sounds-configurator

Hello Officers, Doctors, and Firefighters of Los Santos and Blaine County,

I present you this small script I wrote for managing ELS (Emergency Lighting System) configuration files in Grand Theft Auto V. This script helps to standardize and update the <SOUNDS> section across multiple XML files used by various emergency service vehicles. It's particularly useful for ensuring consistency and efficiency when updating siren and horn configurations.

## Features

- **Bulk Editing**: Quickly update the <SOUNDS> section in multiple XML files based on predefined patterns.
- **Logging**: Logs changes made to each file, including the old and new content of the <SOUNDS> section.
- **Pattern Matching**: Uses regex patterns to match and edit specific files associated with police, ambulance, fire department, and other emergency services.
- **Centralized Configuration**: Easily customize the new <SOUNDS> content for different departments or vehicle types.

## Why needed?
In my personal GTA 5 - LSPDFR installation, I aimed for a lore-friendly experience, ensuring that all aspects of the game. However, managing siren configurations across multiple agencies and vehicle types proved to be a daunting task. Specifically, I created a pack of sirens tailored for different agencies such as SAHP, LSPD + BCSO + FIB + LSSD, EMS, and FD, encompassing around 337 lore-friendly vehicle els-xml config files.

The challenge arose when I needed to synchronize these siren configurations across all 337 XML files associated with each vehicle. Attempting to do this manually quickly became overwhelming and impractical. Faced with this issue, I decided to develop a Python script to automate the process. This script allows for seamless updates to the <SOUNDS> blah blah </SOUNDS> section within each XML file, ensuring that the siren and horn configurations are consistently applied across all vehicles.

I believe this script will not only streamline my own gameplay experience but also be beneficial to others within the GTA 5 modding community who seek to maintain a similar level of customization and immersion. By sharing this tool, I hope to alleviate the manual effort required for managing siren configurations and enable others to effortlessly customize their GTA 5 emergency vehicle setups. 

## Usage

### Prerequisites

- Python 3 installed.
- Please make sure you have renamed the directory location in the script.
- ALWAYS make a backup of your pack_default or whichever folder you are using for the ELS-xml files. I won't be responsible if you don't read the manual/readme properly.

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/els-renamer.git
   cd els-renamer
   ```

2. Rename the directory paths (if needed)

3. Rename the log_file_path (if needed)



### Configuration

1. **Edit Patterns and New Content**: Modify the `police_patterns`, `sahp_patterns`, `lsfd_patterns`, `ems_patterns`, and corresponding `new_*_sounds_content` variables in `rename_els.py` to match your requirements.

2. **Log File Setup**: Ensure the `log_file_path` variable in `bulkELSEdit.py` points to a valid location where the log file can be written.

### Running the Script

Run the script `bulkELSEdit.py`:
```
python bulkELSEdit.py
```

### Logging

Check the log file (`edit_log.txt` by default) for details on the changes made to each file.

## Example

Assume you want to update the siren configurations for all police vehicles. You would update the `police_patterns` and `new_police_sounds_content` variables in `bulkELSEdit.py`, then run the script to apply those changes across all matching XML files.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, make your improvements, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
