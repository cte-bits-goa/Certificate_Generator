# Repository for making CTE Instructor/Mentor and Student Certificates

[![Gitter chat](https://badges.gitter.im/scraping_cte.svg)](https://gitter.im/CTE-Auto-Certificate/community)


Make changes in this canva template (restricted access) [here](https://www.canva.com/design/DAC4FS6sjqk/Rqw4umv6xb8fYy7ey1dazg/view?utm_content=DAC4FS6sjqk&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton)

Download the template and save it in the Certificate_Generator Folder (please use .png format)


Get the CSV of certificate receivers to be filled in the above template. For less error in names feed the CSV to `get_swd.py` like

`python get_swd.py name_of_file.csv`

A numpy array of names extracted from SWD will be created and saved as `swd_names.npy`. Then call `cert_maker.py` arguments as

1. Name of template image
2. Name numpy array of names as obtained ie. `swd_names.npy`
3. Name of Course
4. Type of certificate ie. Instructor/Student
5. Sub-type of certificate ie. Instructor/Mentor in case of Instructor & Completion/Participation incase of Student

Example

`python cert_maker.py "temp_name.png" "swd_names.npy" "Introduction to Robotics" "Instructor" "Instructor" "original_csv.csv"`

A folder with name of the course and type of certificate will be created.

Further feed to automail.
