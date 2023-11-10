# cover_letter_generator
A python script to generate cover letter in Word and PDF format.

The script asks you to input company_name, position_name, relevant_skills, and whether or not you want the cover letter to be converted to PDF format.

company_name: Name of the company
position_name: Name of the position you are applying to
relevant_skills: Relevant skills you have for the above position in the format of "Skill1 Skill2 Skill3"

The script will parse all your skills entered and will change the format to be "Skill1, Skill2, and Skill3".

For example, with the input value of company_name = AWS, position_name = Software Engineer: The file generated have a file name of "Cover_Letter_AWS_Software_Engineer.docx" / "Cover_Letter_AWS_Software_Engineer.pdf"

In your cover_letter_template, make sure to include the above fields in the format of {{ field_name }} and the script will automatically generate the cover letter for you.
