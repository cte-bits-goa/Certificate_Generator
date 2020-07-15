# Repository for making CTE Instructor/Mentor and Student Certificates

[![Gitter chat](https://badges.gitter.im/scraping_cte.svg)](https://gitter.im/CTE-Auto-Certificate/community)


Make changes in this canva template (restricted access) [here](https://www.canva.com/design/DAC4FS6sjqk/Rqw4umv6xb8fYy7ey1dazg/view?utm_content=DAC4FS6sjqk&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton)

Download the template and save it in the Certificate_Generator Folder (please use .png format)


Get the CSV of certificate receivers to be filled in the above template. The csv should contain the following parameters per entry.
1. Name
2. ID
3. Course
4. Instructor/Mentor

To generate certificates, run the cert_maker python file. To file requires three arguments in the following order
1. Certificate template
2. Instructor data in the csv format
3. Message to be entered 

Example

`python cert_maker.py template.png instructor_data.csv message.txt`

Here:
1. `template.png` - the certificate template.
2. `instructor_data.csv` - csv file with instructor data
3. `message.txt` - file containing the message 

A folder named certs with certificates will be generated.

Further feed to automail.
