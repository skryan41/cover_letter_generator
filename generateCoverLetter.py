from docxtpl import DocxTemplate
from docx2pdf import convert
import datetime

# Global Variable for template name of Cover Letter
template_name = "cover_letter_template.doc"


def create_cover_letter(details: dict) -> DocxTemplate:
    """
    Creates the Word document of cover letter with information in details.
    :param details: dictionary of detailed information
    :return: created Word document
    """
    doc = DocxTemplate(template_name)
    doc.render(details)
    doc.save('Cover_letter_' + company_name.replace(' ', '_') + '_' + position_name.replace(' ', '_') + '.docx')
    return doc


def organize_skills(skills: str) -> str:
    """
    Organize skills so that it is in the correct format for the cover letter.
    :param skills: unorganized skills string in the format of skill1 skill2 skill3
    :return: String of organized skills
    """
    split_skills = skills.split(' ')
    if len(split_skills) == 1:
        return skills

    result = ""
    for i, skill in enumerate(split_skills):
        if i == len(split_skills) - 1:
            result += 'and ' + skill
        else:
            result += split_skills[i] + ', '
    return result


if __name__ == "__main__":
    today_date = datetime.datetime.today().strftime('%m/%d/%Y')
    company_name = input("Enter name of the Company : ")
    position_name = input("Enter name of the Position: ")
    relevant_skills = input("Enter the relevant skills you have for this position: ")
    to_convert = input("Convert to PDF (Y/N): ")

    context = {
        'today_date': today_date,
        'company_name': company_name,
        'position_name': position_name,
        'relevant_skills': organize_skills(relevant_skills)
    }

    create_cover_letter(context)
    if to_convert == "Y":
        convert('Cover_letter_' + company_name.replace(' ', '_') + '_' + position_name.replace(' ', '_') + '.docx')
