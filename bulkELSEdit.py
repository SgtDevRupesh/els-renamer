import os
import re

def edit_sounds_section(file_path, new_content):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Find the <SOUNDS> section
        sounds_section_pattern = re.compile(r'<SOUNDS>.*?</SOUNDS>', re.DOTALL)
        old_content = sounds_section_pattern.search(content)
        
        if old_content:
            old_content_str = old_content.group(0)
            # Replace the old <SOUNDS> section with the new content
            new_content_wrapped = f"<SOUNDS>{new_content}</SOUNDS>"
            updated_content = content.replace(old_content_str, new_content_wrapped)
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            
            return old_content_str, new_content_wrapped
        else:
            return None, None
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")
        return None, None

def bulk_edit(directory, patterns, new_content, pattern_name, log_file):
    edited_files = []
    file_groups = {}  # Dictionary to group files by their <SOUNDS> section content
    
    for file_name in os.listdir(directory):
        if any(re.match(pattern, file_name) for pattern in patterns):
            file_path = os.path.join(directory, file_name)
            old_content, new_content_wrapped = edit_sounds_section(file_path, new_content)
            if old_content is not None:
                if old_content not in file_groups:
                    file_groups[old_content] = []
                file_groups[old_content].append((file_name, new_content_wrapped))

    if file_groups:
        log_file.write(f"\nEdited files for pattern '{pattern_name}':\n")
        counter = 0  # Counter for all edited files
        for old_content, files in file_groups.items():
            counter += 1
            log_file.write(f"{counter}. Files with common content:\n")
            for file_name, new_content_wrapped in files:
                log_file.write(f"   - {file_name}\n")
            log_file.write(f"Old content:\n{old_content}\n")
            log_file.write(f"New content:\n{new_content_wrapped}\n\n")

# Directory containing XML files
directory = r'C:\Program Files (x86)\Steam\steamapps\common\Grand Theft Auto V\ELS\pack_default' # Add your directory location!

# Patterns and new content for police files
police_patterns = [
    r'^dw_police', 
    r'^police', 
    r'^policelsia', 
    r'^lspd', 
    r'^dw_lspd', 
    r'^portpolice',
    r'^sheriff', 
    r'^dw_bcso', 
    r'^dw_bcs',
    r'^dw_sheriff', 
    r'^bso',
    r'^dw_dppolice',
    r'^fibp',
    r'^dw_beachp',
    r'^dw_pol',
    r'^poln',
    r'^coroner',
    r'^dw_lssd',
    r'^dw_nysp',
    r'^noose',
    r'^dw_noose',
    r'^pscout',
    r'^poln',
    r'^pol',
    r'^dw_pbus',
    r'^dw_ptruck',
    r'^dw_pvan',
    r'^dw_psuv',
    r'^dw_rhpolice',
    r'^dw_pranger',
    r'^dw_saspa',
    r'^sapr',
    r'^swat',
    r'^dw_ulsa',
    r'^centurion',
    r'^riot',
    r'^cg',
    r'^g6rcv',
    r'^buffalosxumk'
]
new_police_sounds_content = '''
        <MainHorn InterruptsSiren="true" AudioString="SIRENS_AIRHORN" />
        <ManTone1 AllowUse="true" AudioString="VEHICLES_HORNS_SIREN_1" />
        <ManTone2 AllowUse="true" AudioString="VEHICLES_HORNS_SIREN_1" />
        <SrnTone1 AllowUse="true" AudioString="VEHICLES_HORNS_SIREN_1" />
        <SrnTone2 AllowUse="true" AudioString="VEHICLES_HORNS_SIREN_2" />
        <SrnTone3 AllowUse="true" AudioString="VEHICLES_HORNS_POLICE_WARNING" />
        <SrnTone4 AllowUse="true" AudioString="VEHICLES_HORNS_POLICE_WARNING" />
        <AuxSiren AllowUse="true" AudioString="VEHICLES_HORNS_SIREN_1" />
        <PanicMde AllowUse="true" AudioString="VEHICLES_HORNS_POLICE_WARNING" />
'''

# Patterns and new content for sahp files
sahp_patterns = [ 
    r'^sahp',
    r'^hway',
    r'^hwaycar'
]
new_sahp_sounds_content = '''
        <MainHorn InterruptsSiren="true" AudioString="SIRENS_AIRHORN" />
        <ManTone1 AllowUse="true" AudioString="VEHICLES_HORNS_SIREN_1" />
        <ManTone2 AllowUse="true" AudioString="VEHICLES_HORNS_SIREN_1" />
        <SrnTone1 AllowUse="true" AudioString="RESIDENT_VEHICLES_SIREN_WAIL_02" />
        <SrnTone2 AllowUse="true" AudioString="RESIDENT_VEHICLES_SIREN_QUICK_02" />
        <SrnTone3 AllowUse="true" AudioString="RESIDENT_VEHICLES_SIREN_WAIL_02" />
        <SrnTone4 AllowUse="true" AudioString="RESIDENT_VEHICLES_SIREN_QUICK_02" />
        <AuxSiren AllowUse="true" AudioString="VEHICLES_HORNS_SIREN_1" />
        <PanicMde AllowUse="true" AudioString="VEHICLES_HORNS_POLICE_WARNING" />
'''

# Patterns and new content for lsfd files
lsfd_patterns = [
    r'^dw_lsfd',
    r'^bcfd',
    r'^firetruck',
    r'^sanfire'
]
new_lsfd_sounds_content = '''
        <MainHorn InterruptsSiren="true" AudioString="SIRENS_AIRHORN" />
        <ManTone1 AllowUse="true" AudioString="VEHICLES_HORNS_SIREN_1" />
        <ManTone2 AllowUse="true" AudioString="VEHICLES_HORNS_SIREN_2" />
        <SrnTone1 AllowUse="true" AudioString="VEHICLES_HORNS_SIREN_1" />
        <SrnTone2 AllowUse="true" AudioString="VEHICLES_HORNS_SIREN_2" />
        <SrnTone3 AllowUse="true" AudioString="VEHICLES_HORNS_POLICE_WARNING" />
        <SrnTone4 AllowUse="true" AudioString="VEHICLES_HORNS_AMBULANCE_WARNING" />
        <AuxSiren AllowUse="true" AudioString="VEHICLES_HORNS_SIREN_1" />
        <PanicMde AllowUse="true" AudioString="VEHICLES_HORNS_POLICE_WARNING" />
'''

# Patterns and new content for ems/ambulance files
ems_patterns = [
    r'^dw_ems',
    r'^ems',
    r'^ambulance',
    r'^dw_ambulance',
    r'^steedamb',
    r'^dw_lguard',
    r'^lguard'
]
new_ems_sounds_content = '''
        <MainHorn InterruptsSiren="true" AudioString="VEHICLES_HORNS_FIRETRUCK_WARNING" />
        <ManTone1 AllowUse="true" AudioString="RESIDENT_VEHICLES_SIREN_WAIL_01" />
        <ManTone2 AllowUse="true" AudioString="RESIDENT_VEHICLES_SIREN_WAIL_01" />
        <SrnTone1 AllowUse="true" AudioString="RESIDENT_VEHICLES_SIREN_WAIL_01" />
        <SrnTone2 AllowUse="true" AudioString="RESIDENT_VEHICLES_SIREN_QUICK_01" />
        <SrnTone3 AllowUse="true" AudioString="RESIDENT_VEHICLES_SIREN_WAIL_01" />
        <SrnTone4 AllowUse="true" AudioString="RESIDENT_VEHICLES_SIREN_QUICK_01" />
        <AuxSiren AllowUse="false" AudioString="VEHICLES_HORNS_SIREN_1" />
        <PanicMde AllowUse="false" AudioString="VEHICLES_HORNS_POLICE_WARNING" />
'''

# Log file path
log_file_path = r'C:\Program Files (x86)\Steam\steamapps\common\Grand Theft Auto V\ELS\els-script-logging\edit_log.txt' # Add location of the directory where you want the log file to be created

# Ensure the log directory exists
log_directory = os.path.dirname(log_file_path)
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Create and write to the log file
with open(log_file_path, 'w') as log_file:
    # Edit police files and log
    bulk_edit(directory, police_patterns, new_police_sounds_content, "police", log_file)
    
    # Edit sahp files and log
    bulk_edit(directory, sahp_patterns, new_sahp_sounds_content, "sahp", log_file)

    # Edit lsfd files and log
    bulk_edit(directory, lsfd_patterns, new_lsfd_sounds_content, "lsfd", log_file)

    # Edit ems files and log
    bulk_edit(directory, ems_patterns, new_ems_sounds_content, "ems", log_file)

# Print success message
print(f"Editing and logging completed. Check '{log_file_path}' for details.")
