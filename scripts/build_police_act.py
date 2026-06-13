# Generate a new text selectable pdf file for the police act


from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

OUTPUT = r"C:\Users\HP\Projects\AI\Legal_Lens\data\raw\Police_Act_2020.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=2.5*cm,
    leftMargin=2.5*cm,
    topMargin=2.5*cm,
    bottomMargin=2.5*cm,
    title="Nigeria Police Act, 2020",
    author="National Assembly of the Federal Republic of Nigeria",
    subject="Nigeria Police Act, 2020",
)

styles = getSampleStyleSheet()

# Custom styles
center_bold = ParagraphStyle("center_bold", parent=styles["Normal"], alignment=TA_CENTER,
                              fontName="Helvetica-Bold", fontSize=11, spaceAfter=6)
center_normal = ParagraphStyle("center_normal", parent=styles["Normal"], alignment=TA_CENTER,
                                fontSize=10, spaceAfter=4)
heading = ParagraphStyle("heading", parent=styles["Normal"], fontName="Helvetica-Bold",
                          fontSize=10, spaceAfter=4, spaceBefore=8)
body = ParagraphStyle("body", parent=styles["Normal"], fontSize=9.5, spaceAfter=4,
                       leading=14, alignment=TA_JUSTIFY)
body_indent = ParagraphStyle("body_indent", parent=body, leftIndent=1.2*cm)
body_indent2 = ParagraphStyle("body_indent2", parent=body, leftIndent=2.4*cm)
body_indent3 = ParagraphStyle("body_indent3", parent=body, leftIndent=3.6*cm)
section_heading = ParagraphStyle("section_heading", parent=styles["Normal"],
                                  fontName="Helvetica-Bold", fontSize=10,
                                  spaceAfter=4, spaceBefore=10, alignment=TA_CENTER)
part_heading = ParagraphStyle("part_heading", parent=styles["Normal"],
                               fontName="Helvetica-Bold", fontSize=10,
                               spaceAfter=6, spaceBefore=10, alignment=TA_CENTER,
                               textTransform="uppercase")
small = ParagraphStyle("small", parent=body, fontSize=8.5)
toc_style = ParagraphStyle("toc_style", parent=styles["Normal"], fontSize=9, spaceAfter=2, leftIndent=0.5*cm)
toc_indent = ParagraphStyle("toc_indent", parent=styles["Normal"], fontSize=9, spaceAfter=2, leftIndent=1.5*cm)


def SP(n=1):
    return Spacer(1, n * 0.3 * cm)

def HR():
    return HRFlowable(width="100%", thickness=0.5, color=colors.black)

story = []

# ─── PAGE 1: EXPLANATORY MEMORANDUM ──────────────────────────────────────────
story.append(SP(2))
story.append(Paragraph("NIGERIA POLICE ACT, 2020", center_bold))
story.append(SP())
story.append(Paragraph("EXPLANATORY MEMORANDUM", center_bold))
story.append(SP())
story.append(Paragraph(
    "This Act repeals the Police Act Cap. P19, Laws of the Federation, 2004 and enacts the Nigeria Police "
    "Act, 2020 to provide for a more effective and well organised Police Force driven by the principles of "
    "transparency and accountability in its operations and management of its resources.", body))
story.append(SP())
story.append(Paragraph(
    "This Act also establishes an appropriate funding framework for the Police Force in line with what is "
    "obtainable in other Federal Government key institutions in the bid to ensure that all police formations "
    "nationwide are appropriately funded for effective policing.", body))
story.append(SP())
story.append(Paragraph("This Act further:", body))
story.append(SP(0.5))
story.append(Paragraph(
    "(a) &nbsp;&nbsp;&nbsp;enhances professionalism in the Police Force through the provision of "
    "increased training opportunities for police officers and other persons employed by the Police Force; and", body_indent))
story.append(SP(0.5))
story.append(Paragraph(
    "(b) &nbsp;&nbsp;&nbsp;creates an enduring cooperation and partnership between the Police Force "
    "and communities in maintaining peace and combating crimes nationwide.", body_indent))
story.append(PageBreak())

# ─── PAGE 2–4: ARRANGEMENT OF SECTIONS ───────────────────────────────────────
story.append(Paragraph("NIGERIA POLICE ACT, 2020", center_bold))
story.append(SP(0.5))
story.append(Paragraph("Arrangement of Sections", center_bold))
story.append(SP())
story.append(Paragraph("Section:", body))
story.append(SP(0.5))

toc_entries = [
    ("PART I - PRELIMINARY", None),
    ("1.", "General objective."),
    ("2.", "Specific objectives."),
    ("PART II – ESTABLISHMENT, COMPOSITION AND DUTIES OF THE NIGERIA POLICE FORCE", None),
    ("3.", "Establishment, composition and duties of the Nigeria Police Force."),
    ("4.", "Primary functions of the Police Force."),
    ("5.", "Duty of Police Force to enforce certain constitutional provisions, etc."),
    ("6.", "Establishment and functions of the Nigeria Police Council."),
    ("PART III- APPOINTMENT, REMOVAL, FUNCTIONS AND POWERS, ETC. OF INSPECTOR-GENERAL OF POLICE", None),
    ("7.", "Appointment, tenure, removal, etc., of Inspector-General of Police."),
    ("8.", "Command of police in case of active service."),
    ("9.", "Functions and powers of the Inspector-General of Police."),
    ("10.", "Delegation of powers."),
    ("PART IV- APPOINTMENT AND FUNCTIONS ETC. OF THE DEPUTY INSPECTOR-GENERAL OF POLICE, ASSISTANT INSPECTORS-GENERAL OF POLICE, COMMISSIONERS OF POLICE AND OTHER PERSONS INTO THE NIGERIA POLICE FORCE", None),
    ("11.", "Appointment and duties of the Deputy Inspector-General of Police and Assistant Inspector-General of Police."),
    ("12.", "Appointment of Commissioners of Police."),
    ("13.", "Functions of Commissioners of Police of States."),
    ("14.", "Appointment of other persons."),
    ("15.", "Pensions and gratuities."),
    ("16.", "Standing orders."),
    ("PART V - GENERAL ADMINISTRATION", None),
    ("17.", "Oath to be taken by officers on appointment."),
    ("18.", "Recruitment and Police Recruitment Committee."),
    ("19.", "Training programmes."),
    ("20.", "Remuneration."),
    ("21.", "Appointment of supernumerary police officers to protect property."),
    ("22.", "Appointment of supernumerary police officers for employment on administrative duties on police premises."),
    ("23.", "Appointment of supernumerary police officers where necessary in the public interest."),
    ("24.", "Appointment of supernumerary police officers for attachment as orderlies."),
    ("25.", "Provisions supplementary to sections 21 to 23."),
    ("PART VI- FINANCIAL PROVISIONS", None),
    ("26.", "Funding of the Police Force."),
    ("27.", "Expenditures by the Police Force."),
    ("28.", "Estimates."),
    ("29.", "Accounts and audit."),
    ("30.", "Annual report."),
    ("PART VII – POWERS OF POLICE OFFICERS", None),
    ("31.", "Investigation of an allegation by the Police."),
    ("32.", "Arrest generally."),
    ("33.", "Mode of arrest."),
    ("34.", "No unnecessary restraint."),
    ("35.", "Notification of cause of arrest and rights of suspect."),
    ("36.", "Arrest in lieu prohibited."),
    ("37.", "Humane treatment of arrested suspect."),
    ("38.", "Arrest by police officer without warrant."),
    ("39.", "Arrest without warrant by private person."),
    ("40.", "Handing over of an arrested suspect by private person."),
    ("41.", "Arrest for offence committed in presence of a judge or magistrate."),
    ("42.", "When public is bound to assist in arrest."),
    ("43.", "Arrested suspect to be taken immediately to police station."),
    ("44.", "Recording of arrests."),
    ("45.", "Power to break out of a house or place for the purpose of liberation."),
    ("46.", "Inventory of property of arrested suspect."),
    ("47.", "Quarterly report of arrests to the Attorney-General."),
    ("48.", "Power to search."),
    ("49.", "Power to stop and search."),
    ("50.", "Action before a search takes place."),
    ("51.", "General conduct of the search."),
    ("52.", "Search of arrested suspect."),
    ("53.", "Examination of arrested suspect."),
    ("54.", "Where reasonable suspicion never exist."),
    ("55.", "Search of place entered by suspect sought to be arrested."),
    ("56.", "Action after search is carried out."),
    ("57.", "Search record."),
    ("58.", "Search warrant safeguards."),
    ("59.", "Execution of search warrant."),
    ("60.", "Recording of statement of suspect."),
    ("61.", "Refusal to give name and residence."),
    ("62.", "Release on bail of a suspect arrested without warrant."),
    ("63.", "Power to release on bail before charge is accepted."),
    ("64.", "Remedy of suspect detained in custody."),
    ("65.", "Summons."),
    ("66.", "Powers to prosecute."),
    ("67.", "Central Criminal Records Registry."),
    ("68.", "Power to take fingerprints."),
    ("69.", "Police to report to supervising magistrates."),
    ("70.", "Chief magistrate to visit police stations every month."),
    ("PART VIII – WARRANTS", None),
    ("71.", "General authority to issue warrant."),
    ("72.", "Form and requisites of warrant of arrest."),
    ("73.", "Warrant to be issued on complaint only if on oath."),
    ("74.", "Warrant may be issued on any day."),
    ("75.", "Warrant, to whom directed and duration."),
    ("76.", "Warrant of arrest may in exceptional cases be directed to other persons."),
    ("77.", "Execution of warrant and procedure."),
    ("78.", "Power to arrest without possession of warrant."),
    ("79.", "Court may direct particulars of security to be taken on execution of warrant."),
    ("80.", "Warrant issued by the Federal High Court."),
    ("81.", "Re-arrest of suspect escaping."),
    ("82.", "Provisions of sections 43 and 53 to apply to arrests under sections 74 and 79."),
    ("83.", "Public safety and public order."),
    ("PART IX - PREVENTION OF OFFENCES AND SECURITY FOR GOOD BEHAVIOUR", None),
    ("84.", "Police to prevent offences and injury to public property."),
    ("85.", "Information of plan to commit offence."),
    ("86.", "Arrest by police to prevent offences."),
    ("87.", "Prevention by other public officers of offences and injury to public property."),
    ("PART X- PROPERTY FOUND AND UNCLAIMED, ETC.", None),
    ("88.", "Found and unclaimed property."),
    ("89.", "Documentation of arrest, witnesses and death in police station."),
    ("90.", "Missing persons."),
    ("PART XI – ESTABLISHMENT OF THE POLICE REWARD FUND, ETC. AND OTHER PROVISIONS RELATING TO THE POLICE FORCE", None),
    ("91.", "Establishment of the Police Reward Fund."),
    ("92.", "Recognition and commendation for gallantry and exemplary service."),
    ("93.", "Police officer and indebtedness."),
    ("94.", "Exception to debt recovery."),
    ("95.", "Private business and conflict of interest."),
    ("PART XII-OFFENCES", None),
    ("96.", "Offences by a police officer."),
    ("97.", "Apprehension of deserters."),
    ("98.", "Assault on police officer."),
    ("99.", "Refusing to aid police officer assaulted."),
    ("100.", "Drinking of alcohol or use of psychotropic substances and stimulants while on duty."),
    ("101.", "Impersonation of police officer."),
    ("102.", "Obtaining admission into Police Force by fraud."),
    ("103.", "Ordinary course of law not to be interfered with."),
    ("104.", "Persons acquitted by the court not to be tried for the same offence under this Act."),
    ("PART XIII – SPECIAL CONSTABLES", None),
    ("105.", "The Special Constabulary."),
    ("106.", "Appointment of special constables."),
    ("107.", "Resignation, suspension and dismissal of special constables appointed under section 106."),
    ("108.", "Appointment of emergency special constables."),
    ("109.", "Provisions supplementary to section 108."),
    ("110.", "Equipment."),
    ("111.", "Instruction of special constables."),
    ("112.", "Allowances, pensions, etc."),
    ("PART XIV - COMMUNITY POLICING COMMITTEE", None),
    ("113.", "Establishment of Community Policing Committee."),
    ("114.", "Establishment of Divisional Community Policing Committee."),
    ("115.", "Establishment of State Community Policing Committees."),
    ("116.", "Objectives of Community Policing Committees."),
    ("117.", "Duties of community policing officers."),
    ("118.", "Functions of Community Policing Committees."),
    ("119.", "Procedural matters."),
    ("PART XV – TRAFFIC WARDEN SERVICE", None),
    ("120.", "Establishment of Traffic Warden Service."),
    ("121.", "Recruitment of traffic wardens."),
    ("122.", "Declarations by traffic wardens."),
    ("123.", "Tenure of office of traffic wardens."),
    ("124.", "Powers of traffic wardens."),
    ("125.", "Certificate of appointment and discharge."),
    ("126.", "Ranks of traffic wardens."),
    ("127.", "Resignation."),
    ("128.", "Discipline."),
    ("129.", "Provision of equipment."),
    ("130.", "Instruction of traffic warden."),
    ("PART XVI - POLICE PUBLIC COMPLAINTS AND DISCIPLINE", None),
    ("131.", "Establishment of Police Complaints Response Unit."),
    ("132.", "Composition of the Unit."),
    ("133.", "Functions of the Unit."),
    ("134.", "Steps to be taken after investigation."),
    ("PART XVII – MISCELLANEOUS PROVISIONS", None),
    ("135.", "Prohibition against gender discrimination."),
    ("136.", "Application of the Act."),
    ("137.", "Disobeying of unlawful orders."),
    ("138.", "Power to make regulations."),
    ("139.", "Repeal."),
    ("140.", "Savings and transitional provisions."),
    ("141.", "Interpretation."),
    ("142.", "Citation."),
    ("", "Schedule"),
]

for num, desc in toc_entries:
    if desc is None:
        story.append(SP(0.3))
        story.append(Paragraph(num, ParagraphStyle("toc_part", parent=styles["Normal"],
                                                    fontName="Helvetica-Bold", fontSize=9,
                                                    spaceAfter=2)))
    else:
        if num == "":
            story.append(Paragraph(desc, toc_indent))
        else:
            story.append(Paragraph(f"{num}&nbsp;&nbsp;&nbsp;{desc}", toc_indent))

story.append(PageBreak())

# ─── MAIN ACT ─────────────────────────────────────────────────────────────────
story.append(Paragraph("NIGERIA POLICE ACT, 2020", center_bold))
story.append(SP(0.5))
story.append(Paragraph("A Bill", center_bold))
story.append(SP(0.5))
story.append(Paragraph("For", center_bold))
story.append(SP())
story.append(Paragraph(
    "An Act to repeal the Police Act Cap. P19, Laws of the Federation of Nigeria, 2004 and enact "
    "Nigeria Police Act, 2020 to provide the framework for the Police Force and ensure cooperation "
    "and partnership between the police and host communities in maintaining peace, combating "
    "crime, protecting liberties, life and property; and for related matters.", body))
story.append(SP())
story.append(Paragraph("{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } Commencement.", body))
story.append(SP())
story.append(Paragraph("ENACTED by the National Assembly of the Federal Republic of Nigeria:", body))
story.append(SP())

# PART I
story.append(Paragraph("PART I - PRELIMINARY", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>1.</b>&nbsp;&nbsp;&nbsp;The objective of this Act is to provide for a more efficient and effective police service that "
    "is based on the principles of:", body))
story.append(Paragraph("(a) accountability and transparency;", body_indent))
story.append(Paragraph("(b) protection of human rights and fundamental freedoms; and", body_indent))
story.append(Paragraph("(c) partnership with other security agencies.", body_indent))
story.append(SP(0.5))

story.append(Paragraph("<b>2.</b>&nbsp;&nbsp;&nbsp;The specific objectives of this Act are to:", body))
story.append(Paragraph(
    "(a) provide for a Police Force that is more responsive to the needs of the general public and has "
    "entrenched in its operations the values of fairness, justice and equity;", body_indent))
story.append(Paragraph(
    "(b) reposition the Police Force to uphold and safeguard the fundamental rights of every person in Nigeria in its operations;", body_indent))
story.append(Paragraph(
    "(c) bring about a positive change in the public perception of the Police Force by ensuring that its "
    "functions are performed in a manner sensitive to the needs and well-being of the general public;", body_indent))
story.append(Paragraph(
    "(d) empower the Police Force to effectively prevent crimes without threatening the liberty and privacy of persons in Nigeria;", body_indent))
story.append(Paragraph(
    "(e) strengthen the Police Force in the performance of its functions, including safety and security of all persons, communities and property in Nigeria;", body_indent))
story.append(Paragraph(
    "(f) ensure that the police performs its functions by creating the enabling environment to foster cooperation and partnership "
    "between it and the communities it serves to effectively prevent, reduce or eradicate crimes;", body_indent))
story.append(Paragraph(
    "(g) develop professionalism in the Police Force by providing relevant training in all police formations in Nigeria for enhanced performance; and", body_indent))
story.append(Paragraph(
    "(h) respect for rights of victims of crime and an understanding of their needs.", body_indent))
story.append(SP())

# PART II
story.append(Paragraph(
    "PART II – ESTABLISHMENT, COMPOSITION AND DUTIES OF THE NIGERIA POLICE FORCE", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>3.</b>&nbsp;&nbsp;&nbsp;(1) There is established for Nigeria the Nigeria Police Force (in this Act referred to as "
    "\"the Police Force\") which shall, subject to the provisions of the Constitution of the Federal Republic of Nigeria:", body))
story.append(Paragraph("(a) be organised and administered in accordance with the provisions of this Act; and", body_indent))
story.append(Paragraph(
    "(b) have such powers and duties and carry out such responsibilities as are conferred on it under this Act or any other law.", body_indent))
story.append(SP(0.3))
story.append(Paragraph("(2) The Police Force shall consist of:", body))
story.append(Paragraph("(a) all persons who, immediately before the commencement of this Act, were members of the Police Force;", body_indent))
story.append(Paragraph("(b) the Inspector-General of Police;", body_indent))
story.append(Paragraph("(c) persons appointed to offices in the Police Force by the Police Service Commission under Part IV of this Act;", body_indent))
story.append(Paragraph("(d) Special Constables appointed under this Act; and", body_indent))
story.append(Paragraph("(e) such other persons that may be appointed under this Act.", body_indent))
story.append(Paragraph("(3) The hierarchy of the Police Force is as specified in the Schedule to this Act.", body))
story.append(SP(0.5))

story.append(Paragraph("<b>4.</b>&nbsp;&nbsp;&nbsp;The Police Force shall:", body))
story.append(Paragraph(
    "(a) prevent and detect crimes, and protect the rights and freedom of every person in Nigeria as provided in the Constitution, "
    "the African Charter on Human and Peoples Rights and any other law;", body_indent))
story.append(Paragraph("(b) maintain public safety, law and order;", body_indent))
story.append(Paragraph("(c) protect the lives and property of all persons in Nigeria;", body_indent))
story.append(Paragraph(
    "(d) enforce all laws and regulations without any prejudice to the enabling Acts of other security agencies;", body_indent))
story.append(Paragraph("(e) discharge such duties within and outside Nigeria as may be required of it under this Act or any other law;", body_indent))
story.append(Paragraph(
    "(f) collaborate with other agencies to take any necessary action and provide the required assistance or support to persons "
    "in distress, including victims of road accidents, fire disasters, earthquakes and floods;", body_indent))
story.append(Paragraph("(g) facilitate the free passage and movement on highways, roads and streets open to the public; and", body_indent))
story.append(Paragraph("(h) adopt community partnership in the discharge of its responsibilities under this Act or under any other law; and", body_indent))
story.append(Paragraph("(i) vet and approve the registration of private detective schools and private investigative outfits.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>5.</b>&nbsp;&nbsp;&nbsp;(1) The Police Force is responsible for promoting and protecting the fundamental rights of "
    "persons in police custody as guaranteed by the Constitution.", body))
story.append(Paragraph(
    "(2) For the purpose of subsection (1), the Police Force shall collaborate with and maintain close working relationships "
    "with any government agency or relevant private initiatives in the establishment of schemes or mechanisms offering legal "
    "services to accused persons, detainees or accused persons in police custody in need of legal services to ensure that they "
    "have full access to justice as laid down under the relevant provisions of Chapter IV of the Constitution.", body))
story.append(Paragraph(
    "(3) In addition to the provisions of subsections (1) and (2), the Police Force is also charged with the responsibility "
    "for promoting and protecting the fundamental rights of all persons as guaranteed under the African Charter on Human and "
    "Peoples' Rights (Ratification and Enforcement) Act and other international legal instruments on human rights to which Nigeria is a signatory.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>6.</b>&nbsp;&nbsp;&nbsp;(1) There is established for the Police Force the Nigeria Police Council (in this Act referred to "
    "as \"the Council\") which is the highest policy making body in matters relating to the Police Force.", body))
story.append(Paragraph("(2) The Police Council shall consist of:", body))
story.append(Paragraph("(a) the President, who is the Chairman;", body_indent))
story.append(Paragraph("(b) the Governor of each State of the Federation;", body_indent))
story.append(Paragraph("(c) the Chairman of the Police Service Commission; and", body_indent))
story.append(Paragraph("(d) the Inspector-General of Police.", body_indent))
story.append(Paragraph("(3) The functions of the Police Council include:", body))
story.append(Paragraph(
    "(a) the organisation and administration of the Police Force and all other matters relating to the Police Force "
    "(not being matters relating to the use and operational control of the Police Force, or the appointment, disciplinary "
    "control and dismissal of members of the Police Force);", body_indent))
story.append(Paragraph("(b) the general supervision of the Police Force;", body_indent))
story.append(Paragraph("(c) advising the President on the appointment of the Inspector-General of Police; and", body_indent))
story.append(Paragraph(
    "(d) receiving and deliberating on reports and advising the President or Inspector-General of Police on actions to be taken:", body_indent))
story.append(Paragraph(
    "(i) pertaining to policing matters from the States of the Federation and the Federal Capital Territory, Abuja on any crucial "
    "decision of their security committee meetings held during the three months preceding a quarterly meeting of the Police Council, and", body_indent2))
story.append(Paragraph(
    "(ii) on security concerns relating to policing from the States and the Federal Capital Territory, Abuja, and taking such action as it may consider appropriate.", body_indent2))
story.append(Paragraph("(4) The Police Council shall meet at least twice in a year and may hold emergency meetings when necessary.", body))
story.append(Paragraph(
    "(5) The Permanent Secretary, Ministry of Police Affairs, shall serve as secretary to the Police Council and his office shall "
    "provide the necessary secretarial support for the work of the Police Council.", body))
story.append(Paragraph("(6) Subject to the provision of this section, the Police Council shall regulate its own proceedings.", body))
story.append(SP())

# PART III
story.append(Paragraph(
    "PART III- APPOINTMENT, REMOVAL, FUNCTIONS AND POWERS OF INSPECTOR-GENERAL OF POLICE", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>7.</b>&nbsp;&nbsp;&nbsp;(1) The Inspector-General of Police is the head of the Nigeria Police Force and shall "
    "exercise full command and operational control over the Police and all its departments and units.", body))
story.append(Paragraph(
    "(2) The person to be appointed as Inspector-General of Police shall be a senior police officer not below the rank "
    "of an Assistant Inspector-General of Police with the requisite academic qualifications of not less than a first degree "
    "or its equivalent in addition to professional and management experience.", body))
story.append(Paragraph(
    "(3) The Inspector-General of Police shall be appointed by the President on the advice of the Police Council from "
    "among serving members of the Police Force.", body))
story.append(Paragraph(
    "(4) The Inspector-General of Police of shall not be removed from office except for gross misconduct, gross violation "
    "of the Constitution of the Federal Republic of Nigeria or demonstrated incapacity to effectively discharge the duties of the office.", body))
story.append(Paragraph(
    "(5) The Inspector-General of Police shall only be removed from office by the President on the advice of the Police Council.", body))
story.append(Paragraph(
    "(6) The person appointed to the office of the Inspector-General of Police shall hold office for four years.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>8.</b>&nbsp;&nbsp;&nbsp;When required to perform military duties in accordance with the provisions of section 4 of "
    "this Act, such duties entailing service with the Armed Forces of Nigeria or any force for the time being attached thereto "
    "or acting therewith, the Police shall be under the command and subject to the orders of the officer in command of the Armed "
    "Forces in Nigeria, but for the purposes of internal security shall remain under the control of a senior police officer.", body))
story.append(SP(0.5))

story.append(Paragraph("<b>9.</b>&nbsp;&nbsp;&nbsp;(1) The powers and functions of the Inspector-General of Police shall include:", body))
story.append(Paragraph(
    "(a) the development of an overall national policing plan with inputs from the Police Force Headquarters and all the various "
    "police formations nationwide before the end of each financial year, setting out the priorities, objectives, cost implications "
    "and expected outcomes of policing for the next succeeding financial year;", body_indent))
story.append(Paragraph(
    "(b) taking into cognisance the security situation across the country and its population, determine the manpower distribution "
    "of the Police based on its numerical strength after due consultation with the Police Service Commission;", body_indent))
story.append(Paragraph(
    "(c) administer and organise the Police Force into various components, units or groups for overall optimal performance and effectiveness;", body_indent))
story.append(Paragraph(
    "(d) ensuring regular training and re-training of police officers and other staff and personnel of the Police Force and for this "
    "purpose, establish and maintain training institutions or centres for the training of members of the Police Force;", body_indent))
story.append(Paragraph(
    "(e) ensuring the physical, mental and psychological wellbeing of all Police personnel;", body_indent))
story.append(Paragraph("(f) seeing to the welfare and conditions of service of Police personnel; and", body_indent))
story.append(Paragraph(
    "(g) performing such other functions or exercising such powers as may be conferred on him under this Act or any other law.", body_indent))
story.append(Paragraph(
    "(2) The Inspector-General of Police shall, in addition to his functions under this section, ensure the discharge by the Police "
    "Force of the responsibilities referred to under section 5 of this Act, and for this purpose, the Inspector-General of Police shall:", body))
story.append(Paragraph("(a) facilitate access to legal support for suspects, accused persons or detainees in police custody;", body_indent))
story.append(Paragraph(
    "(b) ensure that police officers assigned to work under the relevant scheme provide necessary assistance as may be required by legal counsel; and", body_indent))
story.append(Paragraph(
    "(c) for the purposes of performing the functions under this section, submit to the Attorney-General of the Federation and "
    "National Assembly an annual report on how those responsibilities referred to under section 5(2) of this Act are discharged.", body_indent))
story.append(Paragraph(
    "(3) The Attorney-General of the Federation shall, after a review of the annual report received, send his findings and "
    "recommendations to the President and publish same in his official website.", body))
story.append(Paragraph(
    "(4) The Inspector-General of Police shall by order published in the Federal Government Gazette make detailed provisions and "
    "specifications for the establishment and proper working of the schemes or mechanisms under section 5 of this Act.", body))
story.append(Paragraph(
    "(5) The Inspector-General of Police shall, in performing his functions under this Act, obtain inputs from the Deputy "
    "Inspectors-General and Assistant Inspectors-General of the Zonal Commands on the priority areas of policing for the Zones "
    "and incorporate submissions from Commissioners of Police of the States to be included in the overall national strategic plan "
    "for the next succeeding financial year.", body))
story.append(Paragraph("(6) The Inspector-General of Police may:", body))
story.append(Paragraph("(a) re-engage a retired police officer for a period of two years; and", body_indent))
story.append(Paragraph(
    "(b) upon application by the retired police officer, re-engage him for another period of two years.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>10.</b>&nbsp;&nbsp;&nbsp;(1) The Inspector-General of Police may delegate any of his powers under this Act to any "
    "police officer, as may be appropriate, and such powers may be exercised with respect to the matters or class of matters "
    "specified or defined in the instrument of delegation.", body))
story.append(Paragraph(
    "(2) Guided by the principle of efficiency and effectiveness, and for ease of delegation of powers, the Inspector-General "
    "of Police shall devolve powers to Zonal, States, Area Commands, Divisions and Police Posts to ensure quick response to safety and security needs.", body))
story.append(SP())

# PART IV
story.append(Paragraph(
    "PART IV- APPOINTMENT AND FUNCTIONS ETC. OF THE DEPUTY INSPECTOR-GENERAL OF POLICE, ASSISTANT INSPECTORS-GENERAL OF POLICE, "
    "COMMISSIONERS OF POLICE AND OTHER PERSONS INTO THE NIGERIA POLICE FORCE", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>11.</b>&nbsp;&nbsp;&nbsp;(1) The Police Service Commission, on the recommendation of the Inspector-General of Police "
    "shall appoint for the Police Force such numbers of Deputy Inspectors-General of Police and such numbers of Assistant "
    "Inspectors-General of Police as are required for the efficient performance of the functions of the Police Force.", body))
story.append(Paragraph("(2) A person appointed under subsection (1) shall:", body))
story.append(Paragraph(
    "(a) hold office until promotion, retirement or removal by the Police Service Commission on account of gross misconduct "
    "or incapacity to perform the functions of his office after following due process; and", body_indent))
story.append(Paragraph(
    "(b) perform such functions and responsibilities and exercise such powers as are assigned to him by the Inspector-General of Police.", body_indent))
story.append(Paragraph(
    "(3) The most senior Deputy Inspector-General of Police shall, in the absence from office of the Inspector-General of Police, "
    "act on behalf of the Inspector-General of Police in performing any of the functions and discharging the duties of the "
    "Inspector-General of Police under this Act or under any law or in respect of any function as may be delegated by the Inspector-General of Police.", body))
story.append(Paragraph(
    "(4) On resumption of duty by the Inspector-General of Police, the said Deputy Inspector-General of Police shall furnish reports, "
    "in such form or details as the Inspector-General of Police may specify, of all matters dealt with by the Deputy Inspector-General "
    "of Police in the absence of the Inspector-General of Police from office.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>12.</b>&nbsp;&nbsp;&nbsp;(1) The Police Service Commission shall appoint such numbers of Commissioners of Police as are "
    "required for the efficient performance of the functions of the Police Force.", body))
story.append(Paragraph(
    "(2) The Police Service Commission shall, from among the Commissioners of Police appointed under subsection (1), assign a "
    "Commissioner of Police to a State or to the Federal Capital Territory, Abuja.", body))
story.append(Paragraph(
    "(3) The Commissioners of Police not assigned under subsection (2) may be deployed by the Inspector-General of Police to "
    "head departments and such other operational units of the Police Force.", body))
story.append(Paragraph(
    "(4) The Police Service Commission or Inspector-General of Police, in assigning or deploying, as the case may be, "
    "Commissioners of Police under this section to State commands, departments or unit, shall reflect the principle of federal "
    "character as provided in the Constitution and under the relevant Act.", body))
story.append(Paragraph(
    "(5) A person appointed under subsection (1) shall hold office until promotion, redeployment, retirement or removal by the "
    "Police Service Commission on account of gross misconduct or incapacity to perform the functions of his office as the case maybe.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>13.</b>&nbsp;&nbsp;&nbsp;(1) Subject to the provisions this Act, the Commissioner of Police of a State or the Federal "
    "Capital Territory shall:", body))
story.append(Paragraph("(a) have command and control over the Police in the State he is assigned to;", body_indent))
story.append(Paragraph("(b) exercise powers and perform the functions necessary to give effect to sections 4 of this Act; and", body_indent))
story.append(Paragraph("(c) perform any duty delegated to him by the Inspector-General of Police.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>14.</b>&nbsp;&nbsp;&nbsp;The Police Service Commission shall appoint such other persons to offices in the Police Force "
    "as are required for the effective and efficient performance of the functions of the Police Force on such terms and conditions "
    "as maybe prescribed by the Police Service Commission.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>15.</b>&nbsp;&nbsp;&nbsp;(1) Persons appointed to offices under this Part are entitled to such pensions, gratuities and "
    "other retirement benefits as are prescribed under the Pension Reform Act.", body))
story.append(Paragraph(
    "(2) Nothing in this Act prevents the appointment of a person to any office on terms which preclude the grant of a pension, "
    "gratuity or other retirement benefits in respect of that office.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>16.</b>&nbsp;&nbsp;&nbsp;(1) The Inspector-General of Police may make standing orders relating to operational control of the Police.", body))
story.append(Paragraph(
    "(2) Such standing orders are binding upon all police officers and shall be published in the Federal Government Gazette and in one national daily.", body))
story.append(Paragraph("(3) The Police Service Commission may, subject to the provisions of this Act, make standing orders relating to:", body))
story.append(Paragraph(
    "(a) the appointment, promotion and disciplinary control, including dismissal of persons appointed by it into the Police Force; and", body_indent))
story.append(Paragraph("(b) appeals against dismissal or other disciplinary measures.", body_indent))
story.append(Paragraph(
    "(4) The standing orders made under subsection (1) are binding on all persons appointed by the Police Service Commission "
    "and shall be published in the Federal Government Gazette.", body))
story.append(SP())

# PART V
story.append(Paragraph("PART V - GENERAL ADMINISTRATION", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>17.</b>&nbsp;&nbsp;&nbsp;A person appointed as a member of the Police Force shall, prior to the commencement of duties, "
    "subscribe to the official oath, the police oath and the oath of allegiance under the Oaths Act.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>18.</b>&nbsp;&nbsp;&nbsp;(1) The responsibility for the recruitment of recruit constables into the Nigeria Police Force "
    "and recruit cadets into the Nigeria Police Academy shall be the duty of the Inspector-General of Police.", body))
story.append(Paragraph(
    "(2) For the purpose of subsection (1), there shall be the Nigeria Police Recruitment Committee (in this Act referred to "
    "as \"the Police Recruitment Committee\").", body))
story.append(Paragraph(
    "(3) The Police Recruitment Committee is responsible for the recruitment of recruit constables into the Nigeria Police Force.", body))
story.append(Paragraph("(4) The Police Recruitment Committee shall consist of:", body))
story.append(Paragraph("(a) the Inspector-General of Police as Chairman;", body_indent))
story.append(Paragraph("(b) all the serving Deputy Inspectors-General of Police;", body_indent))
story.append(Paragraph("(c) the Force Secretary;", body_indent))
story.append(Paragraph("(d) the Commandant of Staff College Jos;", body_indent))
story.append(Paragraph("(e) the Commandant of Police Academy Wudil, Kano;", body_indent))
story.append(Paragraph("(f) a representative each of the Police Colleges; and", body_indent))
story.append(Paragraph("(g) the officer in-charge of the legal section of the Nigeria Police Force.", body_indent))
story.append(Paragraph(
    "(5) The recruitment of recruit constables into the Nigeria Police Force shall be of national spread across each State of the Federation.", body))
story.append(Paragraph(
    "(6) The members of the Police Recruitment Committee shall have power to delegate officers, not below the rank of Chief "
    "Superintendent of Police, to represent them at any meeting or recruitment exercise.", body))
story.append(Paragraph(
    "(7) The decision of the Police Recruitment Committee is final on any matter concerning the recruitment of recruit constables "
    "into the Nigeria Police Force.", body))
story.append(Paragraph(
    "(8) Every police officer shall, on recruitment or appointment, serve in the Nigeria Police Force for a period of 35 years "
    "or until he attains the age of 60 years, whichever is earlier.", body))
story.append(Paragraph(
    "(9) Professionals from the relevant fields, including engineering, medicine, pathology, aviation, law, psychology, accountancy "
    "and forensic science, shall:", body))
story.append(Paragraph("(a) be appointed into the Nigeria Police Force as specialists; and", body_indent))
story.append(Paragraph(
    "(b) practise their professions and use their expertise in the advancement of the objectives of the Police Force.", body_indent))
story.append(Paragraph(
    "(10) All candidates wishing to be recruited or appointed into the Nigeria Police Force shall undergo psychological and "
    "other medical evaluations as may be required as part of the recruitment or appointment process to ascertain their character "
    "and suitability for the job.", body))
story.append(Paragraph(
    "(11) Within the period of recruitment or appointment, every police officer shall undergo specialised training in any "
    "professional field relevant to policing and law enforcement.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>19.</b>&nbsp;&nbsp;&nbsp;(1) The Inspector-General of Police shall ensure that all police officers undergo periodic "
    "training and re-training in:", body))
story.append(Paragraph("(a) basic policing, ethics, code of conduct and standard operating procedures;", body_indent))
story.append(Paragraph("(b) crime detection and law enforcement;", body_indent))
story.append(Paragraph("(c) investigation and gathering of evidence;", body_indent))
story.append(Paragraph("(d) effective nationwide citizen engagement;", body_indent))
story.append(Paragraph("(e) human rights, gender issues, public relations and other emerging issues;", body_indent))
story.append(Paragraph("(f) democratic policing and emotional intelligence; and", body_indent))
story.append(Paragraph("(g) prosecution and defence;", body_indent))
story.append(Paragraph(
    "(2) The Inspector-General of Police, in consultation with the Ministry and Police Service Commission, is responsible for "
    "the revision of the training, duration and the content of the training of police officers, at least once in every five years.", body))
story.append(Paragraph(
    "(3) The Inspector-General of Police shall ensure that training programmes are made available to all police officers, "
    "irrespective of gender and for all other staff or employees charged with responsibilities for discharging the duties and "
    "responsibilities of the Police Force.", body))
story.append(Paragraph(
    "(4) All police officers shall undergo periodic training and retraining in basic policing and law enforcement courses as "
    "well as specialized courses relevant to law enforcement.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>20.</b>&nbsp;&nbsp;&nbsp;The police officer shall not be paid salary below what is payable to officers in other "
    "security agencies.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>21.</b>&nbsp;&nbsp;&nbsp;(1) Any private organisation or government department who desires to avail itself of the "
    "services of supernumerary police for the protection of property owned or controlled by it may make application to the "
    "Inspector-General of Police:", body))
story.append(Paragraph("(a) stating the nature and situation of the property in question; and", body_indent))
story.append(Paragraph("(b) giving such other particulars as the Inspector-General of Police may require.", body_indent))
story.append(Paragraph(
    "(2) On an application under subsection (1), the Inspector-General of Police may, with the approval of the Police Service "
    "Commission, direct the appropriate authority to appoint, as supernumerary police officers in the Police Force, such number "
    "of persons as the Inspector-General of Police thinks appropriate for the protection of the property to which the application relates.", body))
story.append(Paragraph(
    "(3) Every supernumerary police officer appointed under this section and sections 22 and 23:", body))
story.append(Paragraph(
    "(a) is appointed in respect of the area of the Police Zonal, State, Area or Divisional Commands in which the personnel "
    "and property which he is to protect are located;", body_indent))
story.append(Paragraph(
    "(b) is employed exclusively on duties connected with the protection, administration and maintenance of that property or premises;", body_indent))
story.append(Paragraph(
    "(c) shall, in the police area in respect of which he is appointed and in any police area adjacent thereto, have the powers, "
    "privileges and immunities of a police officer; and", body_indent))
story.append(Paragraph("(d) shall be:", body_indent))
story.append(Paragraph("(i) a member of the Police Force for all purposes, and", body_indent2))
story.append(Paragraph(
    "(ii) subject to the provisions of this Act, particularly the provisions relating to discipline.", body_indent2))
story.append(Paragraph(
    "(4) Where any supernumerary police officer is appointed, the private or government department availing itself of the "
    "services of that officer shall pay:", body))
story.append(Paragraph(
    "(a) all entitlements, including salary and allowances to the officer monthly;", body_indent))
story.append(Paragraph("(b) on the enlistment of the officer, the full cost of the officer's uniform and accoutrements, including ceremonial dresses, which:", body_indent))
story.append(Paragraph("(i) is the same as the police general duty, and", body_indent2))
story.append(Paragraph(
    "(ii) shall be paid to the Police in a designated account approved by the Inspector-General of Police.", body_indent2))
story.append(Paragraph(
    "(5) Where the private or government department availing itself of the services of any supernumerary police officer desires "
    "the services of that officer to be discontinued, the private or government department shall give at least two months' notice "
    "in writing to the Inspector-General of Police who shall give approval to such request for implementation, and all benefits "
    "of the officer shall be paid within one month of his release.", body))
story.append(Paragraph("(6) All uniforms shall be supplied by the Police Force Quarter Master.", body))
story.append(Paragraph("(7) The supernumerary police shall be a unit of the Police Force.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>22.</b>&nbsp;&nbsp;&nbsp;The appropriate authority may, at the request of any senior police officer, appoint any "
    "person as a supernumerary police officer at an appropriate level in the Police Force for the administration or maintenance "
    "of premises occupied or used for the purposes of the Police Force, but shall not do so in any particular case unless he "
    "is satisfied in the interest of security or discipline that the persons discharging the duties in question are subject to "
    "the provisions of this Act relating to discipline.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>23.</b>&nbsp;&nbsp;&nbsp;(1) If, at any time, the Inspector-General of Police, with the consent of the Police Service "
    "Commission, is satisfied, as regards any police area, that it is necessary in the public interest for supernumerary police "
    "officers to be employed in that area, he may authorise the appropriate authority to appoint persons as supernumerary police "
    "officers in the Police Force in accordance with the authorisation.", body))
story.append(Paragraph(
    "(2) Every authorisation under this section shall be in writing and shall specify the police area to which it relates and "
    "the maximum number of supernumerary police officers who may be appointed under that authorisation.", body))
story.append(Paragraph("(3) Every supernumerary police officer appointed by an authorisation given under this section shall not:", body))
story.append(Paragraph("(a) bear arms; and", body_indent))
story.append(Paragraph("(b) be covered by the provisions relating to pension as stipulated in section 15 of this Act.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>24.</b>&nbsp;&nbsp;&nbsp;(1) The appropriate authority may, at the request of the Inspector-General of Police or "
    "Commissioner of Police of a State, appoint any person as a supernumerary police officer in the Police Force for attachment "
    "as an orderly to:", body))
story.append(Paragraph("(a) a Minister;", body_indent))
story.append(Paragraph("(b) a Commissioner of the Government of a State; or", body_indent))
story.append(Paragraph("(c) a police officer of, or above, the rank of Assistant Commissioner.", body_indent))
story.append(Paragraph("(2) Every supernumerary police officer appointed under this section, shall:", body))
story.append(Paragraph(
    "(a) be employed exclusively on duties connected with the activities of the person to whom he is attached;", body_indent))
story.append(Paragraph(
    "(b) while so employed, have, throughout Nigeria, the powers, privileges and immunities of a police officer;", body_indent))
story.append(Paragraph(
    "(c) may be trained to bear fire arms with the approval of the Inspector General of Police;", body_indent))
story.append(Paragraph(
    "(d) subject to the restriction imposed by paragraph (a) and section 20 of this Act, shall be a member of the Force for all "
    "purposes and shall be subject to the provisions of this Act, particularly the provisions relating to discipline.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>25.</b>&nbsp;&nbsp;&nbsp;(1) Every supernumerary police officer is, on appointment, enlisted to serve in the Police "
    "Force from month to month, and a supernumerary police officer may, at any time, resign his appointment by giving one "
    "month's notice in that behalf to his employer and senior police officer in charge of the police area in respect of which "
    "he is appointed, and his appointment may be determined by the appropriate authority on:", body))
story.append(Paragraph("(a) one month's notice in that behalf; or", body_indent))
story.append(Paragraph("(b) on payment of one month's pay instead of such notice.", body_indent))
story.append(Paragraph(
    "(2) The ranks to which supernumerary police officers may be appointed shall be prescribed by the Inspector-General of Police "
    "with the consent of the Police Service Commission, but shall not exceed the rank of Commissioner of Police throughout his life time.", body))
story.append(Paragraph(
    "(3) There shall only be one Supernumerary Commissioner of Police at a time in the Federation.", body))
story.append(Paragraph(
    "(4) The badges of ranks of the supernumerary police shall be the same as that worn by general duty or regular police.", body))
story.append(Paragraph(
    "(5) A supernumerary police officer has no claim on the Police Reward Fund, and, without prejudice to any liability under "
    "the Employee's Compensation Act, to be paid compensation to or in respect of any person by virtue of his employment as a "
    "supernumerary police officer, a person's service as such shall not render him or any other person eligible for any pension, "
    "gratuity or annual allowance under this Act or the Pensions Reform Act.", body))
story.append(SP())

# PART VI
story.append(Paragraph("PART VI- FINANCIAL PROVISIONS", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>26.</b>&nbsp;&nbsp;&nbsp;(1) There is established and maintained for the Police Force a fund (in this Act referred "
    "to as \"the General Fund\") into which shall be paid:", body))
story.append(Paragraph(
    "(a) budgetary allocations for capital and recurrent expenditure, for members of the Police Force and the Traffic Warden "
    "Service established under this Act and the other staff of the Police Force, as may be appropriated by an Act of the National "
    "Assembly for the Police Force;", body_indent))
story.append(Paragraph(
    "(b) such contributions as may be made available to the Police Force, for the purposes of this Act, by the State Governments "
    "and the Federal Capital Territory, Abuja;", body_indent))
story.append(Paragraph(
    "(c) aid and assistance from international bilateral and multilateral organisations provided that the purpose for the aid or "
    "assistance does not conflict with the objectives of this Act;", body_indent))
story.append(Paragraph(
    "(d) all sums of money accruing to the Police Force by way of grants-in-aid, gifts, testamentary dispositions, endowments "
    "and contributions from any other source;", body_indent))
story.append(Paragraph(
    "(e) all money generated by the Police Force in the course of its operations, including two-thirds of fees paid:", body_indent))
story.append(Paragraph("(i) by members of the public in respect of extracts from police reports, and", body_indent2))
story.append(Paragraph(
    "(ii) in accordance with standing orders for services of police officers who would otherwise be off duty, and", body_indent2))
story.append(Paragraph(
    "(f) any other financial resource that may be vested in or accrue to the Police Force in the course of performing its "
    "functions under this Act or any other law.", body_indent))
story.append(Paragraph(
    "(2) A State Government or the Federal Capital Territory, as the case may be, shall:", body))
story.append(Paragraph("(a) keep records of all contributions made; and", body_indent))
story.append(Paragraph("(b) specify the purpose for which a contribution is made under subsection (1) (b).", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>27.</b>&nbsp;&nbsp;&nbsp;(1) The Police Force shall, from time to time, apply the money accruing in the General Fund to:", body))
story.append(Paragraph("(a) the cost of administration and operations of the Police Force;", body_indent))
story.append(Paragraph(
    "(b) the payment of salaries, allowances, expenses and other benefits of the members of the Police Force and Warden Service "
    "established under this Act and the other staff of the Police Force;", body_indent))
story.append(Paragraph("(c) the payment of pensions and other retirement benefits under any law;", body_indent))
story.append(Paragraph(
    "(d) the costs of acquisition and upkeep of premises belonging to the Police Force and any other capital expenditure of the Police Force;", body_indent))
story.append(Paragraph(
    "(e) all costs connected with or incidental to the operations of the Community Policing Committees and Sub-Committee Forums "
    "and Boards established under Part XIV of this Act;", body_indent))
story.append(Paragraph("(f) the investments, maintenance of utilities, training, research and similar activities; and", body_indent))
story.append(Paragraph(
    "(g) any other payment for anything incidental to the provisions of this section or any other function of the Police Force under this Act.", body_indent))
story.append(Paragraph(
    "(2) Any contribution made by a State Government or the Federal Capital Territory under section 26 (1) (b) or any other "
    "contribution in respect of which a purpose was specified shall be used by the Police Force for the purpose specified.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>28.</b>&nbsp;&nbsp;&nbsp;(1) The Police Force shall, not later than 30th September of each year, submit to the National "
    "Assembly, through the Minister, estimates of its income and expenditure for the next succeeding financial year.", body))
story.append(Paragraph(
    "(2) Notwithstanding the provisions of subsection (1), the Police Force may, where necessary due to unforeseen circumstances, "
    "submit supplementary or adjusted statements of estimated income and expenditure to the Minister for submission to the National Assembly.", body))
story.append(Paragraph(
    "(3) The Police Force shall, in preparing its estimates under this section, obtain inputs from the Force Headquarters, Zonal "
    "Headquarters, State Commands, Area Commands and Divisional Commands on their budgetary needs based on the annual policing "
    "plans for the various policing formations to be included in the overall estimates for the Police Force for the next succeeding financial year.", body))
story.append(SP(0.5))

story.append(Paragraph("<b>29.</b>&nbsp;&nbsp;&nbsp;(1) The Police Force shall:", body))
story.append(Paragraph("(a) keep proper records and accounts of the income and expenditures of the Police Force; and", body_indent))
story.append(Paragraph("(b) prepare a statement of account in respect of each financial year.", body_indent))
story.append(Paragraph(
    "(2) The Police Force shall, within the first four months of each financial year, submit for auditing, the accounts of the "
    "Police Force to auditors appointed by the Police Force from the list and in accordance with guidelines approved by the "
    "Auditor-General for the Federation.", body))
story.append(Paragraph(
    "(3) The audited accounts of the Police Force and the Auditor-General's report on the accounts shall be forwarded to the "
    "National Assembly by the Auditor-General annually.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>30.</b>&nbsp;&nbsp;&nbsp;(1) The Police Force shall, not later than 30th June of each financial year, submit to the "
    "Minister, in respect of the preceding financial year, an annual report on the activities of the Police Force in such form "
    "as the Minister may direct.", body))
story.append(Paragraph("(2) The report under subsection (1) shall include:", body))
story.append(Paragraph(
    "(a) detailed information with regards to the activities and expenditures of the Police Force utilised in the carrying out of its policing plan;", body_indent))
story.append(Paragraph(
    "(b) a copy of the audited accounts of the Police Force for that year together with the Auditor-General's report on the accounts;", body_indent))
story.append(Paragraph(
    "(c) information and description of all contributions made to the Police Force under section 26 (1) (b), including contributions other than cash; and", body_indent))
story.append(Paragraph("(d) such other information as the Minister may request.", body_indent))
story.append(Paragraph(
    "(3) The Police Force shall, from time to time, provide the Police Council, Police Service Commission and Minister with "
    "such information relating to the affairs of the Police Force as they may request.", body))
story.append(SP())

# PART VII
story.append(Paragraph("PART VII – POWERS OF POLICE OFFICERS", part_heading))
story.append(SP(0.3))
story.append(Paragraph("A. Investigation and Arrest", heading))
story.append(SP(0.3))

story.append(Paragraph(
    "<b>31.</b>&nbsp;&nbsp;&nbsp;Where an alleged offence is reported to the Police, or a person is brought to the police "
    "station on the allegation of committing an offence, the Police shall investigate the allegation in accordance with due "
    "process and report its finding to the Attorney-General of the Federation or of a State, as the case may be, for legal advice.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>32.</b>&nbsp;&nbsp;&nbsp;(1) A suspect or defendant alleged or charged with committing an offence established by an Act "
    "of the National Assembly or under any other law shall be arrested, investigated and tried or dealt with according to the "
    "provisions of this Act, except otherwise provided under this Act.", body))
story.append(Paragraph("(2) A person shall not be arrested merely on a civil wrong or breach of contract.", body))
story.append(Paragraph(
    "(3) A suspect shall be brought before the court as prescribed by this Act or any other written law or otherwise released "
    "conditionally or unconditionally.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>33.</b>&nbsp;&nbsp;&nbsp;In making an arrest, the police officer or other persons making the arrest shall actually "
    "touch or confine the body of the suspect, unless there is a submission to the custody by word or action.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>34.</b>&nbsp;&nbsp;&nbsp;A suspect or defendant may not be handcuffed, bound or subjected to restraint except:", body))
story.append(Paragraph("(a) there is reasonable apprehension of violence or an attempt to escape;", body_indent))
story.append(Paragraph("(b) the restraint is considered necessary for the safety of the suspect or defendant; or", body_indent))
story.append(Paragraph("(c) by order of a court.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>35.</b>&nbsp;&nbsp;&nbsp;(1) Except when the suspect is in the actual course of committing an offence or is pursued "
    "immediately after the commission of an offence or has escaped from lawful custody, the police officer or other person "
    "making the arrest shall inform the suspect immediately of the reason for the arrest.", body))
story.append(Paragraph("(2) The police officer, the person making the arrest or the police officer in charge of a police station "
    "shall inform the suspect of his rights to:", body))
story.append(Paragraph(
    "(a) remain silent or avoid answering any question until after consultation with a legal practitioner or any other person of his own choice;", body_indent))
story.append(Paragraph(
    "(b) consult a legal practitioner of his choice before making, endorsing or writing any statement or answering any question "
    "put to him after arrest; and", body_indent))
story.append(Paragraph(
    "(c) free legal representation by the Legal Aid Council of Nigeria or other organisations, where applicable.", body_indent))
story.append(Paragraph(
    "(3) The authority having custody of the suspect shall notify the next-of-kin or relative of the suspect of the arrest at no cost to the suspect.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>36.</b>&nbsp;&nbsp;&nbsp;A person shall not be arrested in place of a suspect.", body))
story.append(SP(0.5))

story.append(Paragraph("<b>37.</b>&nbsp;&nbsp;&nbsp;(1) A suspect shall:", body))
story.append(Paragraph(
    "(a) be accorded humane treatment, having regard to his right to the dignity of his person; and", body_indent))
story.append(Paragraph(
    "(b) not be subjected to any form of torture, cruel, inhuman or degrading treatment.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>38.</b>&nbsp;&nbsp;&nbsp;(1) A police officer may, without an order of a court and without a warrant, arrest a suspect:", body))
story.append(Paragraph(
    "(a) whom he suspects on reasonable grounds of having committed an offence against a law in Nigeria or against the law of any "
    "other country, unless the law creating the offence provides that the suspect cannot be arrested without a warrant;", body_indent))
story.append(Paragraph("(b) who commits an offence in his presence;", body_indent))
story.append(Paragraph(
    "(c) who obstructs a police officer while in the execution of his duty, or who has escaped or attempts to escape from lawful custody;", body_indent))
story.append(Paragraph(
    "(d) in whose possession anything is found which may reasonably be suspected to be stolen property or who may reasonably be "
    "suspected of having committed an offence with reference to the thing;", body_indent))
story.append(Paragraph("(e) whom he suspects on reasonable grounds of being a deserter from any of the armed forces of Nigeria;", body_indent))
story.append(Paragraph(
    "(f) whom he suspects on reasonable grounds of having been involved in an act committed at a place outside Nigeria which, "
    "if committed in Nigeria, would have been punished as an offence, and for which he is, under a law in force in Nigeria, "
    "liable to be apprehended and detained in Nigeria;", body_indent))
story.append(Paragraph(
    "(g) having in his possession without lawful excuse, the burden of proof of which excuse shall lie on the person, any "
    "implement of housebreaking, car theft, firearm or any offensive or dangerous weapon;", body_indent))
story.append(Paragraph(
    "(h) whom he has reasonable cause to believe a warrant of arrest has been issued by a court of competent jurisdiction in Nigeria;", body_indent))
story.append(Paragraph(
    "(i) found in Nigeria taking precautions to conceal his presence in circumstances, which afford reason to believe that he "
    "is taking such precautions with a view to committing an offence;", body_indent))
story.append(Paragraph("(j) whom he is directed to arrest by a judge or magistrate.", body_indent))
story.append(Paragraph(
    "(k) whom he reasonably suspects to be planning to commit an offence for which the police officer may arrest without a "
    "warrant, if it appears to him that the commission of the offence cannot be otherwise prevented; or", body_indent))
story.append(Paragraph("(l) required to appear by a public summons issued under this Act or any other Act.", body_indent))
story.append(Paragraph("(m) to protect a child or other vulnerable person from the suspect in question;", body_indent))
story.append(Paragraph("(n) to prevent the suspect in question from:", body_indent))
story.append(Paragraph("(i) causing physical injury to himself or any other person,", body_indent2))
story.append(Paragraph("(ii) suffering from physical injury,", body_indent2))
story.append(Paragraph("(iii) causing loss of or damage to property;", body_indent2))
story.append(Paragraph(
    "(iv) committing an offence against public decency where members of the public going about their normal business cannot "
    "reasonably be expected to avoid the person in question, or", body_indent2))
story.append(Paragraph("(v) causing an unlawful obstruction of the highway; and", body_indent2))
story.append(Paragraph("(2) No person shall be arrested without warrant except as provided in subsection (1).", body))
story.append(Paragraph(
    "(3) The authority given to a police officer to arrest a suspect who commits an offence in his presence is exercisable in "
    "respect of offences committed in the officer's presence notwithstanding that the Act creating the offence provides that "
    "the suspect cannot be arrested without a warrant.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>39.</b>&nbsp;&nbsp;&nbsp;A private person may arrest a suspect in Nigeria who in his presence commits an offence, or "
    "whom he reasonably suspects of having committed an offence for which the police is entitled to arrest without a warrant.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>40.</b>&nbsp;&nbsp;&nbsp;(1) A private person who arrests a suspect shall immediately hand over the suspect to a police "
    "officer or, in the absence of a police officer, shall take the suspect to the nearest police station, and the police officer "
    "shall make a note of the name, address and other particulars of the private person making the arrest.", body))
story.append(Paragraph(
    "(2) Where there is reason to believe that the arrested suspect comes under subsection (1), a police officer shall re-arrest "
    "him and if there is no sufficient reason to believe that the suspect has committed an offence, he shall be released immediately.", body))
story.append(Paragraph(
    "(3) Where there is reason to believe that the suspect has committed an offence, and he refuses, on the demand of a police "
    "officer, to give his name and address, or gives a name or address which the police officer reasonably believes to be false, "
    "the provisions of section 61 of this Act shall apply.", body))
story.append(Paragraph(
    "(4) Where a suspect so arrested by a private person is handed over to a police officer or an official of an agency authorised "
    "by law to make arrests, the police officer or official shall take note of the name, residential address and other particulars "
    "of the private person making the arrest, and the date, time and other circumstances of the arrest, and where the arrested "
    "suspect is taken to the police station or to the agency, the officer shall make the entries in the crime diary.", body))
story.append(Paragraph(
    "(5) The police officer or official to whom the arrested suspect is handed over by the private person shall obtain from the "
    "private person who made the arrest a formal witness statement setting out the facts and circumstances of the arrest.", body))
story.append(Paragraph(
    "(6) The provisions of section 46 of this Act do not apply to this section unless the suspect arrested and handed over has "
    "been re-arrested in accordance with subsection (2).", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>41.</b>&nbsp;&nbsp;&nbsp;A judge or magistrate may arrest or direct the arrest of a suspect committing an offence in "
    "his presence and shall hand him over to a police officer who shall proceed to take necessary action.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>42.</b>&nbsp;&nbsp;&nbsp;A person is bound to assist a judge, magistrate or police officer or other person reasonably "
    "demanding his aid in arresting or preventing the escape of a suspect whom the judge, magistrate, police officer or other "
    "person is authorised to arrest.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>43.</b>&nbsp;&nbsp;&nbsp;(1) A suspect who is arrested, whether with or without a warrant, shall be taken immediately "
    "to a police station, or other place for the reception of suspect, and shall be promptly informed of the allegation against "
    "him in the language he understands.", body))
story.append(Paragraph(
    "(2) A person who has the custody of an arrested suspect shall give the suspect reasonable facilities for obtaining legal "
    "advice, access to communication for taking steps to furnish bail, and otherwise making arrangements for his defence or release.", body))
story.append(Paragraph(
    "(3) Notwithstanding the provision of subsection (2), any communication or legal advice shall be done or given in the presence "
    "of an officer who has custody of the arrested suspect.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>44.</b>&nbsp;&nbsp;&nbsp;(1) Where a suspect is arrested, whether with or without a warrant, and taken to a police station "
    "or any other agency effecting the arrest, the police officer making the arrest or the officer in charge shall cause to be taken "
    "immediately, in the prescribed form, the following record of the suspect arrested:", body))
story.append(Paragraph("(a) the alleged offence;", body_indent))
story.append(Paragraph("(b) the date and circumstances of his arrest;", body_indent))
story.append(Paragraph("(c) his full name, occupation and residential address; and", body_indent))
story.append(Paragraph("(d) for the purpose of identification:", body_indent))
story.append(Paragraph("(i) his height,", body_indent2))
story.append(Paragraph("(ii) his photograph,", body_indent2))
story.append(Paragraph("(iii) his full fingerprint impressions, or", body_indent2))
story.append(Paragraph("(iv) such other means of his identification.", body_indent2))
story.append(Paragraph(
    "(2) The process of recording in subsection (1) shall be concluded within a reasonable time of the arrest of the suspect, but not exceeding 48 hours.", body))
story.append(Paragraph(
    "(3) Any further action in respect of the suspect arrested under subsection (1) shall be entered in the record of arrests.", body))
story.append(Paragraph(
    "(4) Where a suspect who is arrested, with or without a warrant, volunteers to make a confessional statement, the police "
    "officer shall ensure that the making and taking of the statement shall be in writing and may be recorded electronically on "
    "a retrievable video or audio visual means.", body))
story.append(Paragraph(
    "(5) Notwithstanding the provision of subsection (4), an oral confession of arrested suspect is admissible in evidence.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>45.</b>&nbsp;&nbsp;&nbsp;A police officer or any other person authorised to make an arrest may break out of a house "
    "or place in order to liberate himself or any other person who, having lawfully entered for the purpose of making an arrest, "
    "is detained in the house or place.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>46.</b>&nbsp;&nbsp;&nbsp;(1) A police officer making an arrest or to whom a private person hands over the suspect, shall "
    "immediately record information about the arrested suspect and an inventory of all items or property recovered from the suspect.", body))
story.append(Paragraph(
    "(2) An inventory recorded under subsection (1) shall be duly signed by the police officer and the arrested suspect, but the "
    "failure of the arrested suspect to sign the inventory does not invalidate it.", body))
story.append(Paragraph(
    "(3) The arrested suspect, his legal practitioner or such other person, as the arrested suspect may direct, shall be given a copy of the inventory.", body))
story.append(Paragraph(
    "(4) Where any property has been taken under this section from an arrested suspect, a police officer may, upon request by "
    "either the owner of the property or parties having interest in the property, release such property on bond pending the "
    "arraignment of the arrested suspect before a court.", body))
story.append(Paragraph(
    "(5) Where a police officer refuses to release the property to the owner or any person having interest in the property under "
    "subsection (4), the police officer shall immediately make a report to the court of the fact of the property taken from the "
    "arrested suspect and the particulars of the property.", body))
story.append(Paragraph(
    "(6) The court to which a report is made under subsection (5), may, if it is of the opinion that the property or any portion "
    "of it can be returned in the interest of justice to the safe custody of the owner or person having interest in the property, "
    "direct that the property or any portion of it be returned to the owner or to such person having interest in the property.", body))
story.append(Paragraph(
    "(7) Where any property has been taken from a suspect under this section, and the suspect is not charged before a court but "
    "is released on the ground that there is no sufficient reason to believe that he has committed an offence, any property so "
    "taken from the suspect shall be returned to him, provided the property is neither connected to nor a proceed of an offence.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>47.</b>&nbsp;&nbsp;&nbsp;(1) The Inspector-General of Police and head of every agency authorised by law to make arrests "
    "shall remit quarterly to the Attorney-General of the Federation a record of all arrests made with or without warrant in "
    "relation to Federal offences within Nigeria.", body))
story.append(Paragraph(
    "(2) The Commissioner of Police of a State and the head of every agency authorised by law to make arrest within a State "
    "shall remit quarterly to the Attorney-General of that State a record of all arrests made with or without warrant in relation "
    "to State offences or arrests within the State.", body))
story.append(Paragraph(
    "(3) The report shall contain the full particulars of arrested suspects as prescribed under section 44 of this Act.", body))
story.append(Paragraph(
    "(4) A register of arrests containing the particulars prescribed under section 44 of this Act shall be kept in the prescribed "
    "form at every police station or agency authorised by law to make arrests, and every arrest, whether made with or without "
    "warrant, within the local limits of the police station or agency, or within the Federal Capital Territory, Abuja, shall be "
    "entered accordingly by the officer in charge of the police station or official in charge of the agency as soon as the "
    "arrested suspect is brought to the station or agency.", body))
story.append(Paragraph(
    "(5) The Attorney-General of the Federation shall establish an electronic and manual database of all records of arrests at "
    "the Federal and State level.", body))
story.append(SP(0.5))

story.append(Paragraph("B. Search", heading))
story.append(SP(0.3))

story.append(Paragraph(
    "<b>48.</b>&nbsp;&nbsp;&nbsp;(1) A police officer may seize and retain anything for which a search has been authorised.", body))
story.append(Paragraph(
    "(2) In every case in which property is seized under this section, the person on whose premises it was at the time of "
    "seizure or the person from whom it was taken, if other than the person on whose premises it was, may be summoned or "
    "arrested and brought before a court to account for his possession of the property, and the court shall make such order "
    "on the disposal of the property and may award costs as the justice of the case may require.", body))
story.append(Paragraph(
    "(3) An authority under subsection (2) may only be given when the premises to be searched are, or within the preceding "
    "twelve months have been, in the occupation of any person who has been convicted of receiving stolen property or of "
    "harbouring thieves, or of any offence involving fraud or dishonesty, and punishable by imprisonment.", body))
story.append(Paragraph(
    "(4) While searching the premises, a police officer shall not violate the human rights of persons found in the premises "
    "that is being searched.", body))
story.append(SP(0.5))

story.append(Paragraph("<b>49.</b>&nbsp;&nbsp;&nbsp;(1) A police officer may exercise the power to stop and search in any:", body))
story.append(Paragraph(
    "(a) place the public or any section of the public has access, on payment or otherwise, as of right or by virtue of express "
    "or implied permission; or", body_indent))
story.append(Paragraph(
    "(b) other place to which the public has ready access at the time when he proposes to exercise the power but which is not a private residence.", body_indent))
story.append(Paragraph("(2) A Police officer may detain and search any person or vehicle where:", body))
story.append(Paragraph(
    "(a) reasonable grounds for suspicion exist that the person being suspected is having in his possession; or conveying in any "
    "manner anything which he has reason to believe to have been stolen or otherwise unlawfully obtained;", body_indent))
story.append(Paragraph("(b) reasonable grounds for suspicion exist that such person or vehicle is carrying an unlawful article;", body_indent))
story.append(Paragraph(
    "(c) reasonable grounds for suspicion that incidents involving serious violence may take place within a locality;", body_indent))
story.append(Paragraph("(d) information has been received as to a description of an article being carried or of a suspected offender; and", body_indent))
story.append(Paragraph(
    "(e) a person is carrying a certain type of article at an unusual time or in a place where a number of burglaries or thefts "
    "are known to have taken place recently.", body_indent))
story.append(Paragraph(
    "(3) If, in the course of a search, a police officer discovers an article which he has reasonable grounds for suspecting to "
    "be a stolen or prohibited article, he may seize it.", body))
story.append(Paragraph("(4) An article is prohibited for the purposes of this Part if it is:", body))
story.append(Paragraph("(a) an offensive weapon; or", body_indent))
story.append(Paragraph("(b) an article:", body_indent))
story.append(Paragraph(
    "(i) made or adapted for use in the course of or in connection with an offence to which this section refer, or", body_indent2))
story.append(Paragraph("(ii) intended by the person having it for use by him or by some other person.", body_indent2))
story.append(Paragraph("(5) The offences to which subsection (4)(b)(i) applies are:", body))
story.append(Paragraph("(a) burglary;", body_indent))
story.append(Paragraph("(b) theft; and", body_indent))
story.append(Paragraph(
    "(c) offences related to receiving stolen property or of harbouring thieves, or of any offence involving fraud or dishonesty.", body_indent))
story.append(Paragraph("(6) In this Part \"offensive weapon\" means any article:", body))
story.append(Paragraph("(a) made or adapted for use for causing injury to persons; or", body_indent))
story.append(Paragraph("(b) intended by the person having it for use by him or by some other person.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>50.</b>&nbsp;&nbsp;&nbsp;(1) Where a police officer is exercising the powers under section 51 of this Act he shall, "
    "before carrying out the search, question the person about his behaviour or his presence in circumstances which gave rise to the suspicion.", body))
story.append(Paragraph(
    "(2) If the person to be searched has a satisfactory explanation which makes a search unnecessary or other circumstances "
    "come to the attention of the police officer that make the search unnecessary, no search may take place.", body))
story.append(Paragraph(
    "(3) Before any search of a detained person or vehicle may take place, the officer shall give the person to be searched or "
    "in charge of the vehicle:", body))
story.append(Paragraph("(a) his name and the name of the police station to which he is attached;", body_indent))
story.append(Paragraph("(b) the object of the search; and", body_indent))
story.append(Paragraph("(c) his grounds or authorisation for undertaking the search.", body_indent))
story.append(Paragraph(
    "(4) For any police officer to exercise the power to stop and search, he shall be in uniform or wear visibly a valid police identity card.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>51.</b>&nbsp;&nbsp;&nbsp;(1) Reasonable effort shall be taken to minimise the embarrassment that a person or the person "
    "whose property is being searched may experience.", body))
story.append(Paragraph("(2) The co-operation of the person to be searched shall be sought in every case.", body))
story.append(Paragraph(
    "(3) A forcible search may be used as a last resort only if it has been established that the person being searched is unwilling "
    "to co-operate or resists.", body))
story.append(Paragraph(
    "(4) The length of time for which a person or vehicle may be detained for a search depends on the circumstances, but this "
    "shall be within a reasonable time.", body))
story.append(Paragraph("(5) Searches in public shall be restricted to superficial examination of outer clothing.", body))
story.append(Paragraph(
    "(6) Where it is considered necessary to conduct a more thorough search that requires a person to take off his cloth or headgear, it:", body))
story.append(Paragraph(
    "(a) shall be done out of public view and by an officer of the same sex with the person being searched; and", body_indent))
story.append(Paragraph(
    "(b) may not be made in the presence of anyone of the opposite sex unless the person being searched requests it.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>52.</b>&nbsp;&nbsp;&nbsp;(1) Where a suspect is arrested by a police officer or a private person, the police officer "
    "making the arrest or to whom the private person hands over the suspect may search the suspect if the police officer has "
    "reasonable grounds for believing that the arrested person may present a danger to himself or others.", body))
story.append(Paragraph(
    "(2) A police officer shall also have the power in any such case to search the arrested person for anything:", body))
story.append(Paragraph("(a) which he might use to assist him to escape from lawful custody; or", body_indent))
story.append(Paragraph("(b) which might be evidence relating to an offence.", body_indent))
story.append(Paragraph(
    "(3) Where an arrested suspect is admitted to bail and bail is furnished, he shall not be searched unless there are reasonable "
    "grounds for believing that he has on his person any:", body))
story.append(Paragraph("(a) stolen article;", body_indent))
story.append(Paragraph("(b) instrument of violence or poisonous substance;", body_indent))
story.append(Paragraph("(c) tools connected with the kind of offence which he is alleged to have committed; or", body_indent))
story.append(Paragraph(
    "(d) other articles which may furnish evidence against him in regard to the offence, which he is alleged to have committed.", body_indent))
story.append(Paragraph(
    "(4) The power to search conferred under subsection (2) is only a power to search to the extent that is reasonably required "
    "for the purpose of discovering anything or evidence.", body))
story.append(Paragraph(
    "(5) The powers conferred under this section to search a person are not to be construed as authorising a police officer to "
    "require a person to remove any of his clothing in public.", body))
story.append(Paragraph(
    "(6) A police officer may not search premises in the exercise of the power conferred under subsection (2)(b) unless he has "
    "reasonable grounds for believing that there is evidence for which a search is permitted under that paragraph on the premises.", body))
story.append(Paragraph(
    "(7) A police officer shall place in safe custody all articles other than necessary wearing apparel found on the suspect.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>53.</b>&nbsp;&nbsp;&nbsp;(1) Subject to the provision of this section, an intimate search of a suspect may be carried "
    "out, if a police officer of at least the rank of Assistant Superintendent of Police has reasonable grounds for believing "
    "that the suspect in lawful custody:", body))
story.append(Paragraph("(a) may have concealed on him anything which:", body_indent))
story.append(Paragraph("(i) could be used to cause physical injury to himself or others, and", body_indent2))
story.append(Paragraph(
    "(ii) might so use while he is in police detention or in the custody of a court; or", body_indent2))
story.append(Paragraph(
    "(b) that evidence of the offence alleged to have been committed can only be gotten from examination of the suspect.", body_indent))
story.append(Paragraph(
    "(2) An authorisation under subsection (1) may be given orally or in writing, and where an oral authorisation has been given, "
    "it shall be confirmed in writing as soon as practicable specifying the grounds for the intimate search.", body))
story.append(Paragraph(
    "(3) A police officer carrying out the intimate search shall inform the person who is to be subjected to the search of the:", body))
story.append(Paragraph("(a) purpose for the search; and", body_indent))
story.append(Paragraph("(b) authorisation and grounds for the search.", body_indent))
story.append(Paragraph("(4) An intimate search shall be by way of examination by a suitably qualified person.", body))
story.append(Paragraph(
    "(5) Where an officer of the rank of at least an Assistant Superintendent of Police considers it impracticable for an intimate "
    "search to be by way of examination by a suitably qualified person, the intimate search may be carried out by a police officer "
    "at the rank of Sergeant.", body))
story.append(Paragraph(
    "(6) An intimate search shall be carried out by a suitably qualified person or Sergeant of the same sex as the suspect.", body))
story.append(Paragraph("(7) No intimate search may be carried out except:", body))
story.append(Paragraph("(a) at a police station;", body_indent))
story.append(Paragraph("(b) at a hospital; or", body_indent))
story.append(Paragraph("(c) at some other place used for medical purposes.", body_indent))
story.append(Paragraph(
    "(8) If an intimate search of a person is carried out, the custody record relating to him shall state:", body))
story.append(Paragraph("(a) the authorisation by virtue of which the search was carried out;", body_indent))
story.append(Paragraph("(b) the grounds for giving the authorisation;", body_indent))
story.append(Paragraph("(c) the fact that the appropriate consent was given;", body_indent))
story.append(Paragraph("(d) which parts of his body were searched; and", body_indent))
story.append(Paragraph("(e) why they were searched.", body_indent))
story.append(Paragraph(
    "(9) The information required to be recorded by subsection (8) shall be recorded as soon as practicable after the completion of the search.", body))
story.append(Paragraph(
    "(10) The custody officer at a police station may seize and retain anything which is found on an intimate search of a person, "
    "or cause any such thing to be seized and retained if he:", body))
story.append(Paragraph("(a) believes that the person from whom it is seized may use it to:", body_indent))
story.append(Paragraph("(i) cause physical injury to himself or any other person,", body_indent2))
story.append(Paragraph("(ii) damage property,", body_indent2))
story.append(Paragraph("(iii) interfere with evidence, or", body_indent2))
story.append(Paragraph("(iv) assist him to escape;", body_indent2))
story.append(Paragraph("(b) has reasonable grounds for believing that it may be evidence relating to an offence.", body_indent))
story.append(Paragraph(
    "(11) Where anything is seized under this section, the suspect from whom it is seized shall be told the reason for the "
    "seizure unless he is:", body))
story.append(Paragraph("(a) violent or likely to become violent; or", body_indent))
story.append(Paragraph("(b) incapable of understanding what is said to him.", body_indent))
story.append(Paragraph(
    "(12) Where the appropriate consent for an intimate search of any suspect was refused without good cause, in any proceeding "
    "against that suspect for the offence for which the search was required, the court, judge, magistrate or presiding judicial "
    "officer may draw such inferences from the refusal as it is considered proper.", body))
story.append(Paragraph(
    "(13) Every quarterly report submitted to the Attorney-General pursuant to section 47 of this Act shall contain information "
    "about searches under this section which have been carried out during the period to which it relates.", body))
story.append(Paragraph("(14) The report on the searches referred to under subsection 13 shall include:", body))
story.append(Paragraph("(a) the total number of searches;", body_indent))
story.append(Paragraph("(b) the number of searches conducted by way of examination by a suitably qualified person;", body_indent))
story.append(Paragraph(
    "(c) the number of searches not conducted by a suitably qualified person, but conducted in the presence of such a person; and", body_indent))
story.append(Paragraph("(d) the result of the searches carried out.", body_indent))
story.append(Paragraph("(15) In this section \"suitably qualified person\" means a registered:", body))
story.append(Paragraph("(a) medical practitioner; or", body_indent))
story.append(Paragraph("(b) nurse.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>54.</b>&nbsp;&nbsp;&nbsp;The following shall not be grounds for reasonable suspicions;", body))
story.append(Paragraph(
    "(a) personal attributes, including a person's colour, age, hairstyle or manner of dress;", body_indent))
story.append(Paragraph("(b) previous conviction for possession of an unlawful article; or", body_indent))
story.append(Paragraph("(c) stereotyped images of certain persons or groups as more likely to be committing offences.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>55.</b>&nbsp;&nbsp;&nbsp;(1) Where a person or police officer acting under a warrant of arrest or otherwise having "
    "authority to arrest, has reason to believe that the suspect to be arrested has entered into or is within any house or "
    "place, the person residing in or being in charge of the house or place shall, on demand by the police officer or person "
    "acting for the police officer, allow him free access to the house or place and afford all reasonable facilities to search "
    "the house or place for the suspect sought to be arrested.", body))
story.append(Paragraph(
    "(2) Where access to a house or place cannot be obtained under subsection (1), the person or police officer may enter the "
    "house or place and search it for the suspect to be arrested, and in order to effect an entrance into the house or place, "
    "may break open any outer or inner door or window of any house or place, whether that of the suspect to be arrested or of "
    "any other person or otherwise effect entry into such house or place, if after notification of his authority and purpose, "
    "and demand of admittance duly made, he cannot obtain admittance.", body))
story.append(Paragraph(
    "(3) Where the suspect to be arrested enters a house or place in the actual occupancy of another person being a woman who "
    "by custom or religious practice does not appear in public, the person making the arrest shall:", body))
story.append(Paragraph(
    "(a) before entering the house or place, give notice to the woman that she is at liberty to withdraw; and", body_indent))
story.append(Paragraph(
    "(b) afford her every reasonable opportunity and facility for withdrawing, and may then enter the house or place, but the "
    "notice shall not be necessary where the person making the arrest is a woman.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>56.</b>&nbsp;&nbsp;&nbsp;(1) An officer who has carried out a search shall make a written record unless it is not "
    "practicable to do so, including situations where the number of persons to be searched is large or in situations involving public disorder.", body))
story.append(Paragraph(
    "(2) The records shall be completed and signed by the officer and person being searched on the spot and a copy to be given "
    "to the person being searched or the vehicle driver if it is a vehicle.", body))
story.append(Paragraph(
    "(3) Subject to subsection (2), in case the search record is not available on the spot, the officer that carried out the "
    "search shall advise the person searched or the driver of the vehicle searched, of the police station the person may pick up the search record.", body))
story.append(Paragraph("(4) A searched person may refuse to collect a search record that his signature is not appended on.", body))
story.append(Paragraph(
    "(5) Where the person to be searched is unwilling to provide detailed information about himself, the officer may not detain "
    "him, he shall be allowed to go unless unlawful items are found in his possession or in the vehicle searched.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>57.</b>&nbsp;&nbsp;&nbsp;(1) A search record shall be prepared in the prescribed Form to be known as a National Search Record Form.", body))
story.append(Paragraph("(2) The following information must always be included in the National Search Record Form:", body))
story.append(Paragraph(
    "(a) the name of the person searched or if, he withholds it, description of the person;", body_indent))
story.append(Paragraph("(b) the date of birth of the person searched;", body_indent))
story.append(Paragraph("(c) a note of the person's ethnic origin;", body_indent))
story.append(Paragraph(
    "(d) when a vehicle is searched, a description of the vehicle, including the registration number;", body_indent))
story.append(Paragraph("(e) the object of the search;", body_indent))
story.append(Paragraph("(f) the ground for making the search;", body_indent))
story.append(Paragraph("(g) the date and time the search was made;", body_indent))
story.append(Paragraph("(h) the place where the search was made;", body_indent))
story.append(Paragraph("(i) the result of the search;", body_indent))
story.append(Paragraph("(j) a note of any injury or damage to property resulting from the search; and", body_indent))
story.append(Paragraph("(k) the identity of the officer making the search.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>58.</b>&nbsp;&nbsp;&nbsp;(1) A search warrant is unlawful unless it complies with this section.", body))
story.append(Paragraph("(2) Where a police officer applies for any search warrant, it shall be his duty to state:", body))
story.append(Paragraph("(a) the ground on which he makes the application;", body_indent))
story.append(Paragraph("(b) the law under which the warrant would be issued;", body_indent))
story.append(Paragraph("(c) the premises to be searched; and", body_indent))
story.append(Paragraph("(d) possibly the article or person to be searched.", body_indent))
story.append(Paragraph(
    "(3) An application for a warrant shall be made in writing under oath and supported by necessary information.", body))
story.append(Paragraph("(4) A warrant shall authorise an entry on one occasion only.", body))
story.append(Paragraph("(5) A warrant shall:", body))
story.append(Paragraph("(a) specify the:", body_indent))
story.append(Paragraph("(i) name of the person who applies for it,", body_indent2))
story.append(Paragraph("(ii) date on which it is issued,", body_indent2))
story.append(Paragraph("(iii) law under which it is issued, and", body_indent2))
story.append(Paragraph("(iv) premises to be searched; and", body_indent2))
story.append(Paragraph("(b) identify, as practicable as possible, the article or person to be searched.", body_indent))
story.append(Paragraph("(6) Two copies of a warrant shall be made.", body))
story.append(Paragraph("(7) The two copies shall be clearly certified as copies.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>59.</b>&nbsp;&nbsp;&nbsp;(1) A warrant to enter and search premises may be executed by any police officer.", body))
story.append(Paragraph("(2) Such a warrant may authorise a person to accompany any police officer who is executing it.", body))
story.append(Paragraph(
    "(3) A search warrant may be issued and executed at any time on any day, including a Sunday or public holiday.", body))
story.append(Paragraph(
    "(4) Where the occupier of premises which is to be searched is present at the time when a police officer seeks to execute "
    "a warrant to enter and search, the police officer shall:", body))
story.append(Paragraph(
    "(a) identify himself to the occupier and, if not in uniform, shall produce to the occupier, his official identity card;", body_indent))
story.append(Paragraph("(b) produce the warrant to the occupier; and", body_indent))
story.append(Paragraph("(c) supply the occupier with a copy.", body_indent))
story.append(Paragraph(
    "(5) Where the occupier is not present, but some other person who appears to the police officer to be in charge of the "
    "premises is present, subsection (4) shall take effect as if the occupier is present.", body))
story.append(Paragraph("(6) Upon the execution of a warrant, a police officer shall make an endorsement on it stating whether:", body))
story.append(Paragraph("(a) the articles or persons sought were found; and", body_indent))
story.append(Paragraph("(b) any other articles were seized, other than articles which were sought.", body_indent))
story.append(SP(0.5))

story.append(Paragraph("C. Statements", heading))
story.append(SP(0.3))

story.append(Paragraph(
    "<b>60.</b>&nbsp;&nbsp;&nbsp;(1) Where a suspect is arrested on allegation of having committed an offence, his statement "
    "shall be taken, if he so wishes to make a statement.", body))
story.append(Paragraph(
    "(2) The statement may be taken in the presence of a legal practitioner of his choice, or where he has no legal practitioner "
    "of his choice, in the presence of an officer of the Legal Aid Council of Nigeria or an official of a civil society organization "
    "or a justice of the peace or any other person of his choice, provided that the legal practitioner or any other person "
    "mentioned in this subsection shall not interfere while the suspect is making his statement, except for the purpose of "
    "discharging his duty as a legal practitioner.", body))
story.append(Paragraph(
    "(3) Where a suspect does not understand or speak or write in the English language, an interpreter shall record and read over "
    "the statement to the suspect to his understanding and the suspect shall then endorse the statement as having been made by "
    "him, and the interpreter shall attest to the making of the statement.", body))
story.append(Paragraph(
    "(4) The interpreter shall endorse his name, address, occupation, designation or other particulars on the statement.", body))
story.append(Paragraph(
    "(5) The suspect referred to in subsection (1) shall also endorse the statement with his full particulars.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>61.</b>&nbsp;&nbsp;&nbsp;(1) Where a suspect who, in the presence of a police officer, has committed or has been "
    "accused of committing an offence triable summarily, refuses, on demand of the police officer, to give his name and "
    "residential address, or gives a name or residential address which the officer has reason to believe to be false, he may "
    "be arrested by the officer in order that his name or residential address may be ascertained.", body))
story.append(Paragraph(
    "(2) Where the true name and residential address of the suspect have been ascertain, he shall be released on his entry of "
    "recognisance with or without sureties to appear before a magistrate if so required, but if the person is not resident in "
    "Nigeria, a surety or sureties resident in Nigeria shall secure the recognizance.", body))
story.append(Paragraph(
    "(3) Where the true name and address of the suspect cannot be ascertained within 48 hours from the time of arrest, or if "
    "he fails to execute a recognizance, or, where so required, to furnish sufficient sureties, he shall immediately be brought "
    "before the nearest magistrate having jurisdiction.", body))
story.append(Paragraph(
    "(4) Where the suspect on being brought before the court still refuses, the court may deal with him as it will deal with "
    "an uncooperative witness under this Act.", body))
story.append(SP(0.5))

story.append(Paragraph("D. Release of arrested suspect", heading))
story.append(SP(0.3))

story.append(Paragraph(
    "<b>62.</b>&nbsp;&nbsp;&nbsp;(1) Where a suspect has been taken into police custody without a warrant for an offence other "
    "than an offence punishable with death, an officer in charge of a police station shall inquire into the case and release "
    "the suspect arrested on bail subject to subsection (2), and where it will not be practicable to bring the suspect before "
    "a court having jurisdiction with respect to the offence alleged, within 24 hours after the arrest.", body))
story.append(Paragraph(
    "(2) The police officer in charge of a police station shall release the suspect on bail on his entering into a recognisance "
    "with or without sureties for a reasonable amount of money to appear before the court or at the police station at the time "
    "and place named in the recognizance.", body))
story.append(Paragraph(
    "(3) Where a suspect is taken into custody and it appears to the police officer in charge of the station that the offence "
    "is of a capital nature, the arrested suspect shall be detained in custody, and the police officer may refer the matter to "
    "the Attorney-General of the Federation or of a State, as the case may, for legal advice and cause the suspect to be taken "
    "before a court having jurisdiction with respect to the offence within a reasonable time.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>63.</b>&nbsp;&nbsp;&nbsp;(1) Where a suspect is taken into custody, and it appears to the police officer that the "
    "inquiry into the case cannot be completed immediately, he may discharge the suspect on his entering into a recognizance, "
    "with or without sureties for a reasonable amount, to appear at the police station and at such times as are named in the "
    "recognisance, unless he previously receives notice in writing from the police officer in charge of that police station that "
    "his attendance is not required.", body))
story.append(Paragraph(
    "(2) A recognisance under subsection (1) may be enforced as if it were a recognizance conditional for the appearance of the "
    "said suspect before a magistrate's court or the place in which the police station named in the recognizance is situate.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>64.</b>&nbsp;&nbsp;&nbsp;(1) Where a suspect taken into custody in respect of a non-capital offence is not released on "
    "bail after 24 hours, a court having jurisdiction with respect to the offence may be notified by application on behalf of the suspect.", body))
story.append(Paragraph(
    "(2) The court shall order the production of the suspect detained and inquire into the circumstances constituting the grounds "
    "of the detention and where it deems fit, admit the suspect detained to bail.", body))
story.append(Paragraph("(3) An application for bail under this section may be made orally or in writing.", body))
story.append(SP(0.5))

story.append(Paragraph("E. Miscellaneous", heading))
story.append(SP(0.3))

story.append(Paragraph(
    "<b>65.</b>&nbsp;&nbsp;&nbsp;Any summons lawfully issued by a court may be served by any police officer at any time during "
    "the hours of daylight, which is between 6am to 6pm.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>66.</b>&nbsp;&nbsp;&nbsp;(1) Subject to the provisions of section 174 and 211 of the Constitution and section 106 of "
    "the Administration of the Criminal Justice Act which relates to the powers of the Attorney-General of the Federation and "
    "of a State to institute, take over and continue or discontinue criminal proceedings against any person before any court of "
    "law in Nigeria, a police officer who is a legal practitioner, may prosecute in person before any court whether or not the "
    "information or complaint is laid in his name.", body))
story.append(Paragraph(
    "(2) A police officer may, subject to the provisions of the relevant criminal procedure laws in force at the Federal or "
    "State level, prosecute before the courts those offences which non-qualified legal practitioners can prosecute.", body))
story.append(Paragraph("(3) There shall be assigned to every Police Division at least one police officer:", body))
story.append(Paragraph(
    "(a) who is qualified to practise as legal practitioner in accordance with the Legal Practitioners Act; and", body_indent))
story.append(Paragraph(
    "(b) whose responsibility is to promote human rights compliance by officers of the Division.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>67.</b>&nbsp;&nbsp;&nbsp;(1) There shall be established at the Nigeria Police, a Central Criminal Records Registry.", body))
story.append(Paragraph(
    "(2) For the purposes of subsection (1), there shall be established at every State Police Command a Criminal Records Registry "
    "which shall keep and transmit all records to the Central Criminal Records Registry.", body))
story.append(Paragraph(
    "(3) The State or Federal Capital Territory Police Command, Abuja shall ensure that the decisions of the court in all "
    "criminal trials are transmitted to the Central Criminal Records Registry within 30 days of the judgement.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>68.</b>&nbsp;&nbsp;&nbsp;(1) A police officer shall take and record for the purposes of identification the measurements, "
    "photographs and fingerprint impression of all persons who may be in lawful custody.", body))
story.append(Paragraph(
    "(2) Where a person who has not previously been convicted of any criminal offence is discharged or acquitted by a court, "
    "all records relating to such measurements, photographs and fingerprint impressions including the document of acquittal or "
    "discharge shall be stored in a retrievable form and handed over to such person upon request.", body))
story.append(Paragraph(
    "(3) A police officer shall apply to a court to compel any person in lawful custody, who refuses to submit to the taking "
    "and recording of his measurements, photographs or fingerprint impressions, to submit himself.", body))
story.append(Paragraph(
    "(4) Subject to subsection (3), the court may authorise a police officer to take the measurements, photographs and "
    "finger-print impressions of such person.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>69.</b>&nbsp;&nbsp;&nbsp;(1) An officer in charge of a police station or an official in charge of an agency authorised "
    "to make arrest shall, on the last working day of every month, report to the nearest supervising magistrate the cases of "
    "all suspects arrested without warrant within the limits of their respective stations or agency whether the suspects have "
    "been admitted to bail or not.", body))
story.append(Paragraph(
    "(2) The report shall contain the particulars of the suspects arrested as prescribed under section 44 of this Act.", body))
story.append(Paragraph(
    "(3) The magistrate shall, on receipt of the reports, forward them to the Criminal Justice Monitoring Committee which shall "
    "analyse the reports and advise the Attorney-General of the Federation as to the trends of arrests, bail and related matters.", body))
story.append(Paragraph(
    "(4) The Attorney-General of the Federation shall, upon request by the National Human Rights Commission, the Legal Aid "
    "Council of Nigeria or a non-governmental organisation, make the report available to them.", body))
story.append(Paragraph(
    "(5) Where no report is made in accordance with subsection (1), the magistrate shall forward a report to the Chief Judge "
    "of the State and the Attorney-General of the State for appropriate remedial action.", body))
story.append(Paragraph(
    "(6) With respect to the Federal Capital Territory, Abuja, the report referred to in subsection (5) shall be forwarded to "
    "the Chief Judge of the Federal Capital Territory, Abuja and the Attorney-General of the Federation for remedial action.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>70.</b>&nbsp;&nbsp;&nbsp;(1) The chief magistrate, or where there is no chief magistrate within the police division, "
    "any magistrate designated by the Chief Judge for that purpose, shall, at least every month, conduct an inspection of "
    "police stations or other places of detention within his territorial jurisdiction other than the prison.", body))
story.append(Paragraph("(2) During a visit, the magistrate may:", body))
story.append(Paragraph("(a) call for, and inspect, the record of arrests;", body_indent))
story.append(Paragraph("(b) direct the arraignment of a suspect;", body_indent))
story.append(Paragraph(
    "(c) where bail has been refused, grant bail to any suspect, where appropriate, if the offence for which the suspect is "
    "held is within the jurisdiction of the magistrate.", body_indent))
story.append(Paragraph(
    "(3) An officer in charge of a police station or an official in charge of an agency authorised to make an arrest shall "
    "make available to the visiting chief magistrate or designated magistrate exercising his powers under subsection (1):", body))
story.append(Paragraph("(a) the full record of arrest and record of bail;", body_indent))
story.append(Paragraph("(b) applications and decisions on bail made within the period; and", body_indent))
story.append(Paragraph("(c) any other facility the magistrate requires to exercise his powers under that subsection.", body_indent))
story.append(Paragraph(
    "(4) With respect to other Federal Government agencies authorised to make arrests, the High Court having jurisdiction "
    "shall visit such detention facilities for the purpose provided in this section.", body))
story.append(Paragraph(
    "(5) Where there is default by an officer in charge of a police station or an official in charge of an agency authorised "
    "to make arrest to comply with the provisions of subsection (3), the default shall be treated as a misconduct and shall "
    "be dealt with in accordance with the relevant police regulations under this Act, or under any other disciplinary procedure "
    "prescribed by any provision regulating the conduct of the officer or official of the agency.", body))
story.append(SP())

# PART VIII
story.append(Paragraph("PART VIII – WARRANTS", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>71.</b>&nbsp;&nbsp;&nbsp;Where under a law, there is power to arrest a suspect without warrant, a warrant for his "
    "arrest may be issued by the court.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>72.</b>&nbsp;&nbsp;&nbsp;(1) A warrant of arrest issued under this Act, unless the contrary is provided under any "
    "other law, shall:", body))
story.append(Paragraph("(a) bear the date of issue;", body_indent))
story.append(Paragraph("(b) contain all necessary particulars; and", body_indent))
story.append(Paragraph("(c) be signed by the issuing judge or magistrate.", body_indent))
story.append(Paragraph("(2) A warrant shall:", body))
story.append(Paragraph("(a) state the offence or matter for which it is issued;", body_indent))
story.append(Paragraph("(b) name and describe the suspect to be arrested; and", body_indent))
story.append(Paragraph(
    "(c) order the person to whom it is directed to arrest the suspect and bring him before the court.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>73.</b>&nbsp;&nbsp;&nbsp;A warrant of arrest shall not be issued in the first instance in respect of any complaint or "
    "statement unless the complaint or statement is on oath either by the complainant himself or by a material witness.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>74.</b>&nbsp;&nbsp;&nbsp;A warrant of arrest may be issued on any day, including a Sunday or public holiday.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>75.</b>&nbsp;&nbsp;&nbsp;(1) A warrant of arrest may be directed to a police officer by name or to all police officers.", body))
story.append(Paragraph(
    "(2) It is not necessary to make a warrant of arrest returnable at any particular time and a warrant shall remain in force "
    "until it is executed or until a judge or a magistrate cancels it.", body))
story.append(Paragraph(
    "(3) Where a warrant of arrest has been executed and the suspect arrested has been released, the warrant shall no longer "
    "be valid authority for re-arresting the suspect.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>76.</b>&nbsp;&nbsp;&nbsp;(1) A court issuing a warrant of arrest may, where its immediate execution is necessary and "
    "no police officer is immediately available, direct it to some other person or persons and the person or persons shall "
    "execute the warrant.", body))
story.append(Paragraph(
    "(2) A person, when executing a warrant of arrest directed to him, shall have all the powers, rights, privileges and "
    "protection given to or afforded by law to a police officer executing a warrant of arrest and shall conform with the "
    "requirement imposed by law on a police officer.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>77.</b>&nbsp;&nbsp;&nbsp;(1) A warrant of arrest may be executed on any day, including a Sunday or public holiday.", body))
story.append(Paragraph(
    "(2) A warrant of arrest may be executed by any police officer at any time and in any place in any State other than within "
    "the actual court room in which a court is sitting.", body))
story.append(Paragraph(
    "(3) The Police officer executing a warrant of arrest shall, before making the arrest, inform the suspect to be arrested "
    "that there is a warrant for his arrest unless there is reasonable cause for abstaining from giving the information on the "
    "ground that it is likely to occasion escape, resistance or rescue.", body))
story.append(Paragraph(
    "(4) A suspect arrested on a warrant of arrest shall, subject to the provisions of the Constitution, sections 80 and 81 "
    "of this Act, be brought before the court that issued the warrant of arrest.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>78.</b>&nbsp;&nbsp;&nbsp;A warrant of arrest may be executed notwithstanding that it is not in the possession of the "
    "person at the time of executing the warrant, but the warrant shall, on the demand by the suspect, be shown to him within 24 hours.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>79.</b>&nbsp;&nbsp;&nbsp;(1) A court, on issuing a warrant for the arrest of a suspect in respect of a matter other "
    "than an offence punishable with death, may, if it deems fit by endorsement on the warrant, direct that the suspect named "
    "in the warrant to be released on bail on his entering into such a recognizance for his appearance as may be required in the endorsement.", body))
story.append(Paragraph("(2) The endorsement shall specify:", body))
story.append(Paragraph("(a) the number of sureties, if any;", body_indent))
story.append(Paragraph(
    "(b) the amount in which they and the suspect named in the warrant are, respectively, to be bound, or are to provide as "
    "cash security on the request of the surety or suspect;", body_indent))
story.append(Paragraph("(c) the court before which the arrested suspect is to attend; and", body_indent))
story.append(Paragraph(
    "(d) the time at which the suspect is to attend, including an undertaking to appear at a subsequent time as may be directed "
    "by any court before which he may appear.", body_indent))
story.append(Paragraph(
    "(3) Where an endorsement is made, the officer in charge of a police station to which on arrest the suspect named in the "
    "warrant is brought, shall discharge him on his entering into a recognizance, with or without sureties approved by that "
    "officer, in accordance with the endorsement, condition for his appearance before the court and at the time and place named in the recognisance.", body))
story.append(Paragraph(
    "(4) Where security is taken under this section, the officer who takes the recognizance shall cause it to be forwarded to "
    "the court before which the suspect named in the recognizance is bound to appear.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>80.</b>&nbsp;&nbsp;&nbsp;(1) A warrant of arrest issued by a Federal High Court sitting anywhere in Nigeria may be "
    "executed in any part of Nigeria.", body))
story.append(Paragraph(
    "(2) A warrant issued under this section may be executed in accordance with section 75 of this Act.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>81.</b>&nbsp;&nbsp;&nbsp;Where a suspect in lawful custody escapes or is rescued, the person from whose custody he "
    "escaped or is rescued or any other person may pursue and re-arrest him in any place in Nigeria.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>82.</b>&nbsp;&nbsp;&nbsp;The provisions of sections 43 and 53 of this Act shall apply to arrests under sections 74 "
    "and 79 of this Act, although the person making such arrest is not acting under a warrant and is not a police officer "
    "having authority to arrest.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>83.</b>&nbsp;&nbsp;&nbsp;(1) The Police Force is responsible for maintaining and securing public safety and public order.", body))
story.append(Paragraph("(2) The Police Force shall, in carrying out its responsibilities under subsection (1):", body))
story.append(Paragraph("(a) uphold the provisions of the Constitution and other laws;", body_indent))
story.append(Paragraph("(b) uphold and protect the fundamental rights of all persons in Nigeria; and", body_indent))
story.append(Paragraph(
    "(c) be fair to all persons in Nigeria notwithstanding their economic status or religious, ethnic or political beliefs and affiliations.", body_indent))
story.append(Paragraph(
    "(3) Subject to the provisions of subsection (1), the Commissioner of Police of a State is responsible for maintaining "
    "security, public safety and public order within the State.", body))
story.append(Paragraph(
    "(4) Where a person or organisation notifies the police of his or its intention to hold a public meeting, rally or procession "
    "on a public highway, or such meetings in a place where the public has access to, the police officer responsible for the area "
    "where the meeting, rally or procession will take place, shall mobilise personnel to provide security cover for the meeting, "
    "rally or procession.", body))
story.append(SP())

# PART IX
story.append(Paragraph(
    "PART IX - PREVENTION OF OFFENCES AND SECURITY FOR GOOD BEHAVIOUR", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>84.</b>&nbsp;&nbsp;&nbsp;(1) A police officer may intervene for the purpose of preventing, and shall, to the best of "
    "his ability, prevent the commission of an offence.", body))
story.append(Paragraph(
    "(2) A police officer may of his authority intervene to prevent an injury attempted to be committed in his presence to any "
    "public property, whether movable or immovable, or the removal of or injury to any public landmark or buoy or other mark "
    "used for navigation.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>85.</b>&nbsp;&nbsp;&nbsp;A police officer receiving information of a plan to commit any offence shall communicate the "
    "information to the police officer to whom he is subordinate, and to any other officer whose duty it is to prevent or take "
    "cognizance of the commission of the offence.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>86.</b>&nbsp;&nbsp;&nbsp;Notwithstanding the provisions of this Act or any other law relating to arrest, a police "
    "officer on a reasonable suspicion of a plan to commit an offence, may arrest, without orders from a magistrate and without "
    "warrant, the suspect where it appears to the officer that the commission of the offence cannot otherwise be prevented.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>87.</b>&nbsp;&nbsp;&nbsp;(1) A judge, magistrate, or any other public officer charged with responsibility for "
    "maintaining law and order may intervene to prevent the commission of an offence or any damage to any public property, "
    "movable or immovable.", body))
story.append(Paragraph(
    "(2) A person is bound to assist a judge or magistrate or police officer or any other public officer reasonably demanding "
    "his aid:", body))
story.append(Paragraph(
    "(a) in preventing the commission of an offence or any damage to any public property, movable or immovable;", body_indent))
story.append(Paragraph(
    "(b) in the suppression of a breach of the peace or in the prevention of any damage to any property, movable or immovable "
    "or to any railway, canal, water supply, telecommunication system, oil pipeline, oil installation, electrical installation; or", body_indent))
story.append(Paragraph(
    "(c) in the prevention of the removal of any public landmark, buoy or other mark used for navigation.", body_indent))
story.append(SP())

# PART X
story.append(Paragraph("PART X- PROPERTY FOUND AND UNCLAIMED, ETC.", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>88.</b>&nbsp;&nbsp;&nbsp;(1) Where a police officer or any other person finds a lost property, the police officer or "
    "person who finds the property shall take it to the nearest police station within 24 hours after it is found.", body))
story.append(Paragraph("(2) A police officer on duty shall collect the property which was found and make a record of it.", body))
story.append(Paragraph(
    "(3) A register shall be kept at a police station for the purpose of making entries of the property found and brought to "
    "the station which shall contain:", body))
story.append(Paragraph("(a) the type of property found;", body_indent))
story.append(Paragraph(
    "(b) the description of the property stating the general particulars and state and condition of the property when it was "
    "brought to the police station and any other relevant information relating to the property;", body_indent))
story.append(Paragraph("(c) the date and time it was found and brought;", body_indent))
story.append(Paragraph(
    "(d) the name, address and telephone number, if any, of the person who found and brought the property to the station;", body_indent))
story.append(Paragraph("(e) the name and rank of the police officer who collected the property; and", body_indent))
story.append(Paragraph(
    "(f) the signatures of the police officer and the person who found and brought the property to the station.", body_indent))
story.append(Paragraph(
    "(4) A police officer who collects the lost and found property shall enter the details in the register referred to in "
    "subsection (3) and prepare two forms acknowledging the receipt of the lost and found property and give a duly signed "
    "copy to the person who found and brought the property to the police station.", body))
story.append(Paragraph(
    "(5) The police officer in charge of the police station in possession of the property found shall make a public announcement "
    "at least on three consecutive times in the print and electronic media about the lost and found property and give a duly "
    "custody of the police station for the rightful owner to claim the property with authentic proof of ownership within a "
    "period of six months.", body))
story.append(Paragraph(
    "(6) The police officer in charge of the station in possession of the property shall release the property upon satisfactory proof of ownership.", body))
story.append(Paragraph(
    "(7) Where the property remains unclaimed after the expiration of six months, the police officer in charge of that police "
    "station shall bring the property before a magistrate court for auction and the proceeds shall be paid into the Police "
    "Reward Fund established under section 91of this Act.", body))
story.append(Paragraph(
    "(8) Where a property in Police custody is a perishable article or its custody involves unreasonable expense or inconvenience, "
    "it may be sold at any time, and the proceeds of sale shall be paid into the Police Reward Fund established under section 91 of this Act.", body))
story.append(Paragraph(
    "(9) There shall be deducted from the proceeds of a sale under subsections (7) and (8), before being paid into the Police "
    "Reward Fund the cost, if any, of the sale and of any sum which the court may direct to be paid as a reward to any person "
    "by whom the property was delivered into the possession of the police.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>89.</b>&nbsp;&nbsp;&nbsp;(1) Where a person appears in a police station in respect of an offence or an allegation of "
    "the commission of an offence either as an accused person or a witness, or as a relation or friend of an accused person "
    "or a witness, the duty officer or such other officer as may be authorised by the officer-in-charge of the police station "
    "shall enter in the official record book:", body))
story.append(Paragraph("(a) the name of the person and his national identity number, if any;", body_indent))
story.append(Paragraph("(b) the date of birth of the person;", body_indent))
story.append(Paragraph("(c) the reason for the person's visits;", body_indent))
story.append(Paragraph("(d) the name and address of the person's next-of-kin;", body_indent))
story.append(Paragraph("(e) the exact time the person comes to the station and leaves, for everyday he visits; and", body_indent))
story.append(Paragraph("(f) any ailment or medical condition which the person has.", body_indent))
story.append(Paragraph(
    "(2) The particulars mentioned in subsection (1) shall be updated each day the person remains in custody in the police station.", body))
story.append(Paragraph(
    "(3) Where, in the discharge of the police duty, a person is shot, wounded or killed, the officer commanding the operation shall record:", body))
story.append(Paragraph(
    "(a) the number of those wounded or killed, the names of the victims or their description as much as possible; and", body_indent))
story.append(Paragraph("(b) efforts taken to ensure hospitalisation of the wounded or proper preservation of the dead.", body_indent))
story.append(Paragraph(
    "(4) A police officer who fails to keep appropriate records referred to in subsections (1), (2) and (3) commits a serious "
    "misconduct, which shall attract disciplinary measure.", body))
story.append(Paragraph(
    "(5) The Inspector-General of Police shall give a quarterly report to the Police Service Commission itemising the number "
    "and identity of persons who:", body))
story.append(Paragraph("(a) were detained in all police formations across Nigeria;", body_indent))
story.append(Paragraph("(b) were charged and prosecuted in the courts in Nigeria and the outcome of their cases;", body_indent))
story.append(Paragraph("(c) were killed or wounded during police operations across Nigeria; and", body_indent))
story.append(Paragraph("(d) died in police custody.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>90.</b>&nbsp;&nbsp;&nbsp;(1) A person who is aware that a person under his employment or control is missing shall, "
    "within 24 hours report to the police:", body))
story.append(Paragraph("(a) the identity of the missing person; and", body_indent))
story.append(Paragraph("(b) circumstances in which that person got missing.", body_indent))
story.append(Paragraph(
    "(2) When a report is made to the police under subsection (1) of this section, the duty officer or such other designated "
    "staff shall immediately record the name and address of the missing person and the person who made the report.", body))
story.append(SP())

# PART XI
story.append(Paragraph(
    "PART XI – ESTABLISHMENT OF THE POLICE REWARD FUND, ETC. AND OTHER PROVISIONS RELATING TO THE POLICE FORCE", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>91.</b>&nbsp;&nbsp;&nbsp;(1) There is established for the Nigeria Police the Police Reward Fund (in this Act referred "
    "to as \"the Reward Fund\") into which shall be paid:", body))
story.append(Paragraph("(a) all money levied by order of a senior officer on members of the police for offences against discipline;", body_indent))
story.append(Paragraph("(b) all fines levied for assaults on members of the police;", body_indent))
story.append(Paragraph(
    "(c) one-third of fees paid by members of the public in respect of extracts from reports made by the police;", body_indent))
story.append(Paragraph(
    "(d) one-third of fees paid in accordance with Standing Orders for the services of police officers who would otherwise be off duty; and", body_indent))
story.append(Paragraph("(e) all sums ordered to be paid into the Fund under section 88 (7) of this Act.", body_indent))
story.append(Paragraph(
    "(2) Subject to the rules for the time being in force under section 23 of the Finance Control and Management Act, the "
    "Reward Fund shall be applied and disbursed at the direction of the Inspector-General of Police, based on criteria laid "
    "by the Police Service Commission:", body))
story.append(Paragraph("(a) to reward members of the police for exemplary services", body_indent))
story.append(Paragraph(
    "(b) for payment of ex gratia compassionate gratuities to widows or children of deceased members of the force;", body_indent))
story.append(Paragraph(
    "(c) for making ex gratia payments towards the funeral expenses of any member of the police who dies in the service of the police: and", body_indent))
story.append(Paragraph(
    "(d) for such other purpose as may be determined, by the Nigerian Police Council.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>92.</b>&nbsp;&nbsp;&nbsp;Police officers who have distinguished themselves with their outstanding performance in the "
    "discharge of their duties shall be duly honoured and recognised for their gallant and exemplary service by the Police Force:", body))
story.append(Paragraph(
    "(a) by recommendation for national honours, attention being paid to deserving officers inclusive;", body_indent))
story.append(Paragraph(
    "(b) through public presentation of awards and certificates of exemplary service from communities and civil society; or", body_indent))
story.append(Paragraph(
    "(c) by the police setting aside a day or week in every year to celebrate outstanding performance by its officers and to "
    "remember their fallen heroes.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>93.</b>&nbsp;&nbsp;&nbsp;(1) A police officer shall not get himself involved in indebtedness of any kind while still "
    "in service, and where he does, he shall be disciplined and the debt or liability shall be recovered from his remuneration "
    "if the creditor can prove the indebtedness by withholding from the police officer's remuneration an amount not exceeding "
    "one-third of his monthly remuneration until the amount of the debt or liability is made good.", body))
story.append(Paragraph(
    "(2) Where the recovery of the debt or liability is by a court order, the court making the order shall give due notice to "
    "the senior police officer in charge of the command to which the indebted officer belongs, and the amount ordered shall "
    "be withheld or deducted from the indebted officer's remuneration until the amount of the debt is made good.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>94.</b>&nbsp;&nbsp;&nbsp;The remuneration of a police officer shall not be withheld on account of any debt or liability "
    "which he may have incurred before being appointed to the police.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>95.</b>&nbsp;&nbsp;&nbsp;A police officer shall not, while in service, be directly involved in managing and running "
    "any private business or trade except farming.", body))
story.append(SP())

# PART XII
story.append(Paragraph("PART XII-OFFENCES", part_heading))
story.append(SP(0.5))

story.append(Paragraph("<b>96.</b>&nbsp;&nbsp;&nbsp;(1) A police officer who:", body))
story.append(Paragraph("(a) begins, raises, abets, countenances, or excites mutiny;", body_indent))
story.append(Paragraph("(b) causes or joins in any sedition or disturbance of any nature whatsoever;", body_indent))
story.append(Paragraph(
    "(c) being at an assembly tending to riot, does not use his utmost endeavour to suppress the assembly;", body_indent))
story.append(Paragraph(
    "(d) coming to the knowledge of any mutiny, or intended mutiny does not without delay give information of the mutiny to his superior officer;", body_indent))
story.append(Paragraph(
    "(e) strikes or offers any violence to his superior officer, while in the execution of his duty;", body_indent))
story.append(Paragraph("(f) deserts or aids or abets the desertion of an officer from the Nigeria Police;", body_indent))
story.append(Paragraph("(g) on enlistment falsely states that he:", body_indent))
story.append(Paragraph("(i) has not been convicted or imprisoned for a criminal offence, or", body_indent2))
story.append(Paragraph(
    "(ii) was never employed by the Government of the Federation or of a State;", body_indent2))
story.append(Paragraph(
    "(h) fails to come to the aid or to assist any person in need of assistance at the time of distress:", body_indent))
story.append(Paragraph(
    "(i) shall be subject to appropriate disciplinary proceedings in accordance with the police disciplinary mechanisms, and", body_indent2))
story.append(Paragraph(
    "(ii) if found liable, shall be recommended for dismissal and charged to court for prosecution in accordance with the relevant laws in force.", body_indent2))
story.append(Paragraph("(2) A police officer shall not, in discharging his duty:", body))
story.append(Paragraph("(a) discriminate against a person in Nigeria, based on the person's-", body_indent))
story.append(Paragraph(
    "(i) place of origin, (ii) gender, (iii) socio-economic status, (iv) ethnic, political or religious affiliation, or "
    "(v) any form of disability, and", body_indent2))
story.append(Paragraph(
    "(b) use a language, or act in such a way that suggests a bias towards a particular group.", body_indent))
story.append(Paragraph(
    "(3) A police officer may be proceeded against for desertion without reference to the time during which he may have been "
    "absent, and may be found guilty, either of desertion or of absence without leave.", body))
story.append(Paragraph(
    "(4) A police officer shall not be convicted as a deserter or of attempting to desert unless the court is satisfied that "
    "there was an intention on the part of the officer either not to return to the Police Force, or to escape some particular important service.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>97.</b>&nbsp;&nbsp;&nbsp;On reasonable suspicion that a person is a deserter, a police officer or any other person "
    "may apprehend him and bring him immediately before a court having jurisdiction in the place where he was found, which may "
    "deal with the suspected deserter or refer him to a court having jurisdiction in the place in which he has deserted.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>98.</b>&nbsp;&nbsp;&nbsp;A person who assaults, obstructs or resists a police officer in the discharge of his duty, "
    "or aids or incites any other person to assault, obstruct or resist a police officer or other person aiding or assisting "
    "the police officer in the discharge of his duty, commits an offence and is liable on conviction to a fine of N500,000 or "
    "imprisonment for a term of six months or both.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>99.</b>&nbsp;&nbsp;&nbsp;Where a person is called upon to aid and assist a police officer who is, while in the discharge "
    "of his duty, assaulted or resisted or in danger of being assaulted or resisted, and the person refuses or neglects to aid "
    "and assist, the person commits an offence and is liable on conviction to a fine of N100,000 or imprisonment for a term of "
    "three months or both.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>100.</b>&nbsp;&nbsp;&nbsp;(1) While on duty, a police officer shall not take any intoxicating liquor, psychotropic "
    "substances or stimulants, where he does, he shall be punished in accordance with the police disciplinary procedures.", body))
story.append(Paragraph("(2) A person who:", body))
story.append(Paragraph(
    "(a) knowingly harbours or entertains, or either directly or indirectly, gives any intoxicating liquor, psychotropic "
    "substance or stimulant to any police officer while on duty, or permits any such police officer to abide or remain in his "
    "house unlawfully; except in cases of extreme urgency,", body_indent))
story.append(Paragraph(
    "(b) by threats or by offer of money, gift, spirits, liquors, psychotropic substances or stimulants induces or attempts "
    "to induce any police officer to commit a breach of his duty as a police officer or to omit any part of such duty, commits "
    "an offence and is liable on conviction to a fine of at least N50,000.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>101.</b>&nbsp;&nbsp;&nbsp;A person not being a police officer who:", body))
story.append(Paragraph(
    "(a) puts on or assumes either in whole or in part, the apparel, name, designation, or description of any police officer "
    "or resembling and intended to resemble the apparel, name or designation of any police officer, or", body_indent))
story.append(Paragraph(
    "(b) In any way pretends to be a police officer for the purpose of obtaining admission into any house or other place, or "
    "of doing any act which such person would not by law be entitled to do of his own authority, commits an offence and is "
    "liable, on summary conviction to a fine of at least N100,000 or imprisonment for at least one year or both.", body_indent))
story.append(SP(0.5))

story.append(Paragraph("<b>102.</b>&nbsp;&nbsp;&nbsp;(1) A person who:", body))
story.append(Paragraph(
    "(a) knowingly uses or attempts to pass off any forged or false certificate, character, letter, or any other document "
    "for the purpose of obtaining admission into the Nigeria Police Force; or", body_indent))
story.append(Paragraph(
    "(b) on applying for enlistment, makes any false answer to any statement put to him by any appropriate authority, commits "
    "an offence and, on summary conviction to a fine of N50,000 or imprisonment for three months or both.", body_indent))
story.append(Paragraph(
    "(2) A police officer may arrest without a warrant any person whom he reasonably believes or suspects of having committed "
    "an offence under this section.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>103.</b>&nbsp;&nbsp;&nbsp;Nothing in this Act is be construed to exempt a police officer from being proceeded against "
    "by the ordinary course of law when accused of any offence punishable under any other Act or law.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>104.</b>&nbsp;&nbsp;&nbsp;(1) A person who has been acquitted by a court of any offence shall not be tried on the same "
    "charge or suffer any punishment under this Act.", body))
story.append(Paragraph(
    "(2) Where a police officer has been convicted by a court for an offence, he is not liable to be punished for the same "
    "offence under this Act, but may have his rank or grade reduced or be dismissed from the Police Force.", body))
story.append(SP())

# PART XIII
story.append(Paragraph("PART XIII – SPECIAL CONSTABLES", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>105.</b>&nbsp;&nbsp;&nbsp;(1) The Special Constabulary is established under this Act.", body))
story.append(Paragraph(
    "(2) The Special Constabulary is deemed part of the Nigeria Police Force, and accordingly references in this Act to the "
    "Police Force shall, subject to the provisions of this Act, include, and be deemed always to have included, references to "
    "the Special Constabulary.", body))
story.append(Paragraph("(3) The Special Constabulary shall consist of-", body))
story.append(Paragraph(
    "(a) special constables appointed in normal circumstances under section 106 of this Act; and", body_indent))
story.append(Paragraph(
    "(b) such emergency special constables as may be appointed from time to time under section 108 of this Act.", body_indent))
story.append(Paragraph(
    "(4) If any enactment requires police officers to perform military duties or confers power (whether expressly or in general "
    "terms) to require police officers to perform such duties, that enactment shall not, in the absence of express provision "
    "to the contrary, extend to members of the special constables.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>106.</b>&nbsp;&nbsp;&nbsp;(1) Subject to the provisions of this section, the competent authority may appoint as a "
    "special constable any person who:", body))
story.append(Paragraph("(a) has attained the age of 21 years but has not attained the age of 50 years;", body_indent))
story.append(Paragraph("(b) is of good character and physically fit; and", body_indent))
story.append(Paragraph("(c) has signified willingness to serve as a special constable.", body_indent))
story.append(Paragraph(
    "(2) The Inspector-General of Police shall, from time to time by notice published in the Force Administrative Instructions, "
    "fix the maximum number of persons who may hold appointments under this section, and a person shall not be appointed as a "
    "special constable under this section if his appointment would cause the number, for the time being so fixed, to be exceeded.", body))
story.append(Paragraph("(3) Subject to subsection (2), the Inspector-General of Police may:", body))
story.append(Paragraph(
    "(a) review the maximum number of persons who may hold appointments under this section in any territory; and", body_indent))
story.append(Paragraph(
    "(b) fix the maximum number of persons appointed under this section who may hold any particular rank in the special "
    "constabulary in any territory;", body_indent))
story.append(Paragraph(
    "(c) in either case, fix different numbers with respect to different territories, and every competent authority shall "
    "ensure that the numbers fixed under this subsection are not exceeded.", body_indent))
story.append(Paragraph("(4) Every special constable appointed under this section-", body))
story.append(Paragraph(
    "(a) shall be appointed to serve as a special constable for one year or such longer period as may be agreed between him "
    "and the authority by whom he is appointed, and shall, on appointment, sign an engagement in the prescribed form to serve "
    "as a special constable for that period;", body_indent))
story.append(Paragraph(
    "(b) shall be appointed in respect of the Police Area Command or, where there is no Police Area Command, the Police "
    "Division in which he resides or is employed;", body_indent))
story.append(Paragraph(
    "(c) shall, within the territory in which the police area in respect of which he is appointed is situated, but not "
    "elsewhere, have the powers, privileges and immunities of a special constable; and subject to the provisions of this Act, "
    "shall be a member of the special constable for all purposes:", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>107.</b>&nbsp;&nbsp;&nbsp;(1) A special constable appointed under section 106 of this Act may, at any time, give to "
    "the senior police officer in charge of the police area in respect of which he is appointed notice in writing to the effect "
    "that he desires to resign his appointment on a date (not being less than 30 days later than the date on which the notice "
    "is given) mentioned in the notice.", body))
story.append(Paragraph(
    "(2) On receipt of a notice under subsection (1), the senior police officer in question shall refer it to the competent "
    "authority, and if the competent authority consents to the notice, the appointment of the special constable by whom the "
    "notice was given shall determine on the date mentioned in the notice or the date on which he is notified that the "
    "competent authority has given its consent under this subsection, whichever, is the later.", body))
story.append(Paragraph(
    "(3) The competent authority may, at any time for reasons appearing to it to be sufficient by notice in writing, immediately "
    "suspend or determine the appointment of any special constable appointed under section 106 and may, if it deems fit, do so "
    "without informing the special constable of the reasons for his action, but shall in every case immediately report its "
    "action and the reasons to the Inspector-General of Police.", body))
story.append(Paragraph(
    "(4) A special constable whose appointment is suspended or determined under subsection (3) otherwise than by the "
    "Inspector-General of Police, may appeal against the suspension or determination to the competent authority, and any such "
    "appeal shall be heard and determined by the competent authority to whom it is made.", body))
story.append(Paragraph(
    "(5) Any delegation of the powers of the Inspector-General of Police under subsections (3) and (4) shall be such as to "
    "secure that in every case the competent authority having power to hear and determine an appeal under subsection (4) is a "
    "police officer of higher rank than the police officer against whose action the appeal is brought.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>108.</b>&nbsp;&nbsp;&nbsp;(1) If at any time the Commissioner of Police for a State or Federal Capital Territory is "
    "satisfied, as police in that State, that an unlawful assembly or riot or breach of the has taken may reasonably be expected "
    "to take place in that area, or that by reason of other special circumstance it in necessary in the public interest for "
    "emergency special constables to be appointed in respect of that area, he may authorise the senior police officer in charge "
    "of that area or any Chief Superintendent of Police to appoint person resident or employed in that area (whether male or "
    "female) emergency special constables.", body))
story.append(Paragraph(
    "(2) An authorisation under this section need not be in writing, but shall specify the maximum number of emergency special "
    "constables who may be appointed under that authorisation.", body))
story.append(Paragraph(
    "(3) Where a senior police officer proposes to appoint any person as an emergency special constable under an authorisation "
    "given under this section, he shall cause to be served on that person a notice in the prescribed form requiring him to "
    "present himself at a time and place specified in the notice for appointment as an emergency special constable.", body))
story.append(Paragraph(
    "(4) Every person on whom a notice is served under subsection (3) shall present himself at the time and place specified in "
    "the notice and shall, on being required to do so by the senior police officer proposing to appoint him, make and sign a "
    "promise in the prescribed form to serve as an emergency special constable until such time as his appointment is determined "
    "under this section, and immediately after he has made and signed that promise, the senior police officer shall hand to him "
    "a document in the prescribed form appointing him as an emergency special constable in respect of the police area to which "
    "the authorisation under which he is being appointed relates.", body))
story.append(Paragraph("(5) Every emergency special constable:", body))
story.append(Paragraph(
    "(a) shall, in the police area in respect of which he is appointed, not elsewhere, have the powers, privileges and "
    "immunities of a special constable; and", body_indent))
story.append(Paragraph("(b) subject to the provisions of this Act, shall be a member of the special constabulary for all purposes.", body_indent))
story.append(Paragraph(
    "(6) The senior police officer in charge of the police area in respect of which an emergency special constable is appointed "
    "may at any time, and shall, if so directed by the Commissioner of Police for the State in which that police area is situated, "
    "by notice in writing forthwith, or with effect from a future date specified in the notice, determine the emergency special "
    "constable's appointment, and on the determination of his appointment under this section, an emergency special constable "
    "shall be issued with a certificate of discharge in the prescribed form.", body))
story.append(Paragraph("(7) Any person who, without reasonable excuse (proof of which shall lie on him):", body))
story.append(Paragraph(
    "(a) refuses or fails to comply with the requirements of a notice served on him under subsection (3); or", body_indent))
story.append(Paragraph(
    "(b) refuses to make and sign a promise to serve on being required to do so under subsection (3) is liable on summary "
    "conviction to a fine not exceeding N10,000.", body_indent))
story.append(Paragraph(
    "(8) The provisions of this section shall apply in relation to the Federal Capital Territory, Abuja as they apply in "
    "relation to a State, subject to the modification that, in relation to the Federal Capital Territory. Abuja any reference "
    "to the Commissioner of Police shall be construed as a reference to the Inspector-General of Police.", body))
story.append(Paragraph(
    "(9) The provisions of this section shall have effect subject to section 106 (2) and (3) of this Act.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>109.</b>&nbsp;&nbsp;&nbsp;(1) The Commissioner of Police for a State or Federal Capital Territory or the "
    "Inspector-General of Police;", body))
story.append(Paragraph(
    "(a) on giving an authorisation under section 108 of this Act, shall forthwith inform the President of his action and of "
    "the circumstances which led him to take it, and shall as soon as possible cause notice of the giving of the authorisation "
    "to be published in the Force Administrative Instructions; and", body_indent))
story.append(Paragraph(
    "(b) as soon as possible after all emergency special constables appointed under that authorisation have been discharged, "
    "shall cause notice of that fact to be published in the Force Administrative Instructions.", body_indent))
story.append(Paragraph(
    "(2) The Inspector-General of Police may, by order published in the Force Administrative Instructions, declare persons of "
    "any class or description specified in the order to be exempted from appointment as emergency special constables under "
    "section 108 of this Act, and the power to appoint persons as emergency special constables under that section shall not "
    "extend to persons of any class or description for the time being so specified.", body))
story.append(Paragraph(
    "(3) Any power to make or determine appointments under or by virtue of section 108 of this Act shall be exercisable only "
    "while there is in force the necessary delegation of that power by the Inspector-General of Police.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>110.</b>&nbsp;&nbsp;&nbsp;(1) The Inspector-General of Police may provide for use by special constables such as "
    "batons, clothing and other equipment as he considers necessary for the proper carrying out of their duties.", body))
story.append(Paragraph(
    "(2) Any expenses incurred by the Inspector-General of Police under this section shall be defrayed out of the funds of the Police Force.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>111.</b>&nbsp;&nbsp;&nbsp;(1) Regulation made under section 139 (1) (a) of this Act with respect to the organisation "
    "and administration of the Force shall not require special constables to attend for instruction on more than four days in "
    "any one month or for periods in the aggregate to more than 24 hours in any one month.", body))
story.append(Paragraph(
    "(2) Any person responsible for giving instruction to special constables under the regulations shall have regard as far as "
    "possible to the convenience of special constables who are to attend for instruction also, where applicable, to that of "
    "the employers of such special constables.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>112.</b>&nbsp;&nbsp;&nbsp;(1) Except as expressly provided by this section or by regulations made under subsection "
    "(3), a person's service as a special constable shall render him for a stipend as may be determined by the Inspector-General "
    "of Police as approved by Police Council.", body))
story.append(Paragraph("(2) A special constable shall:", body))
story.append(Paragraph("(a) have no claim on the Police Reward Fund; and", body_indent))
story.append(Paragraph(
    "(b) not as such be entitled to occupy living accommodation provided at the public expense.", body_indent))
story.append(Paragraph(
    "(3) Regulations made under section 139 (1) (a) of this Act may provide for stipends to be paid to special constables-", body))
story.append(Paragraph(
    "(a) in respect of expenses incurred by them in connection with their attendance at periods of instruction;", body_indent))
story.append(Paragraph("(b) as compensation for loss of earnings during periods of full-time duty; and", body_indent))
story.append(Paragraph(
    "(c) in respect of the use by special constables or of this subsection, the rank of Inspector of their own vehicles while "
    "on full-time duty, but shall not provide for the payment of any other stipends to special constables; and the amount of "
    "any such stipends as is mentioned in paragraph (a) or of this subsection shall be fixed by the regulations, and shall "
    "not be calculated by reference to the actual expenses or loss of earnings of the person to whom it is payable.", body_indent))
story.append(SP())

# PART XIV
story.append(Paragraph("PART XIV - COMMUNITY POLICING COMMITTEE", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>113.</b>&nbsp;&nbsp;&nbsp;(1) For the effective and efficient policing of communities in a State or Federal Capital "
    "Territory, the Commissioner of Police of a State shall establish Community Policing Committee (in this Act referred to as "
    "\"the Policing Committee\") which shall consist of representatives of the Police Force and the local community in the State.", body))
story.append(Paragraph(
    "(2) A Commissioner of Police of a State shall establish Community Sub-Policing Committee (in this Act referred to as "
    "\"the Sub-Policing Committees\") at all Divisional Police Headquarters in the State or Federal Capital Territory.", body))
story.append(Paragraph(
    "(3) Subject to section 116 (1) (b) of this Act, the Commissioner of Police and members designated by him from time to "
    "time for the purpose, shall be members of the Policing Committees and Sub-Policing Committees established at various police formations.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>114.</b>&nbsp;&nbsp;&nbsp;(1) A Commissioner of Police of a State or Federal Capital Territory shall, in collaboration "
    "with the relevant stakeholders in the community, establish Divisional Community Policing Committee (in this Act referred "
    "to as \"Divisional Policing Committee\") in all Police Divisions within the State.", body))
story.append(Paragraph(
    "(2) A Divisional Policing Committee shall, in collaboration with the relevant stakeholders in the community, establish "
    "Divisional Community Policing Sub-Committee in all police formations in the Division.", body))
story.append(Paragraph(
    "(3) Subject to section 116 (1) (b) of this Act, the Divisional Police Officer and the members designated by him, from "
    "time to time for that purpose, shall be members of the Divisional Policing Committee concerned.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>115.</b>&nbsp;&nbsp;&nbsp;(1) A Commissioner of Police of a State shall, in collaboration with the State Executive "
    "Council, establish a State Community Sub-Policing Committee.", body))
story.append(Paragraph(
    "(2) A State Community Policing Committee shall, subject to subsection (3), consist of representatives of Divisional "
    "Community Policing Committees designated for that purpose by the Divisional Community Policing Committees of a State concerned.", body))
story.append(Paragraph(
    "(3) Subject to section 116 (1) (b) of this Act, the Commissioner of Police in a State and the members designated by him, "
    "from time to time for the purpose, shall be members of the State Community Policing Committee concerned.", body))
story.append(SP(0.5))

story.append(Paragraph("<b>116.</b>&nbsp;&nbsp;&nbsp;(1) The objectives of the Committees are to:", body))
story.append(Paragraph("(a) maintain a partnership between the community and the Police Force;", body_indent))
story.append(Paragraph("(b) promote communication between the Police Force and the community;", body_indent))
story.append(Paragraph(
    "(c) promote co-operation between the Police and the community in fulfilling the needs of the community regarding policing;", body_indent))
story.append(Paragraph("(d) improve the police service to the community; and", body_indent))
story.append(Paragraph(
    "(e) improve transparency and accountability in the provision of police services to the community.", body_indent))
story.append(Paragraph(
    "(2) This section does not prevent police liaison with the community by means other than Policing Committee, Sub-Policing "
    "Committee and Divisional Policing Committee.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>117.</b>&nbsp;&nbsp;&nbsp;(1) The duties of community policing officers shall include assisting the Police in:", body))
story.append(Paragraph("(a) crime detection and prevention;", body_indent))
story.append(Paragraph("(b) conflict resolution;", body_indent))
story.append(Paragraph("(c) criminal intelligence gathering and dissemination to the local Police Commanders;", body_indent))
story.append(Paragraph("(d) maintenance of law and order;", body_indent))
story.append(Paragraph(
    "(e) deployment to complement the conventional Police in the patrol of the public space within their local communities;", body_indent))
story.append(Paragraph(
    "(f) reassuring and advising the public on public safety, crime prevention and security tips;", body_indent))
story.append(Paragraph("(g) dealing with minor offences and social vices;", body_indent))
story.append(Paragraph(
    "(h) working with the community, schools, and young people, business communities, religious bodies, cultural groups, "
    "community-based associations, recreational centres and hospitality businesses toward crime control; and", body_indent))
story.append(Paragraph("(i) traffic management and school safety duties.", body_indent))
story.append(Paragraph(
    "(2) The Inspector-General of Police, in implementing community policing, shall promote organisational strategies that "
    "support the systematic use of partnerships and problem-solving techniques to proactively address conditions that cause "
    "crime, social disorder and fear of crime.", body))
story.append(Paragraph(
    "(3) The Inspector-General of Police in implementing community policing may vary strategies according to the needs of the "
    "communities involved and the cultural context and local models which will vary and evolve according to the differing needs "
    "of differing communities, whilst retaining and sharing the same set of goals and basic principles.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>118.</b>&nbsp;&nbsp;&nbsp;A State Community Policing Committee or Divisional Community Policing Sub-Committee shall "
    "perform the functions it deems necessary and appropriate to achieve the objectives stated in section 116 of this Act.", body))
story.append(SP(0.5))

story.append(Paragraph("<b>119.</b>&nbsp;&nbsp;&nbsp;(1) A Committee, Sub-Committee and Divisional Committee shall:", body))
story.append(Paragraph(
    "(a) elect, from amongst its members, a chairman, vice-chairman and a secretary who shall be police officers;", body_indent))
story.append(Paragraph(
    "(b) determine the number of members to be assigned by the State Commissioner or Divisional Police Officer to serve as "
    "members of the Committee or Sub-Committee concerned;", body_indent))
story.append(Paragraph("(c) determine its own procedure and cause minutes to be kept of its proceedings; and", body_indent))
story.append(Paragraph(
    "(d) whenever it considers necessary, co-opt other members, experts or community leaders to the Committee, Sub-Committee "
    "and Divisional Committee in an advisory capacity.", body_indent))
story.append(Paragraph(
    "(2) Members of the Committee, Sub-Committee and Divisional Committee shall render their services on a voluntary basis "
    "and shall have no claim to any remuneration solely for services rendered to the Committee, Sub-Committee or Divisional Committee.", body))
story.append(Paragraph(
    "(3) The majority of the members of a Committee, Sub-Committee or Divisional Committee shall constitute a quorum at any of its meetings.", body))
story.append(Paragraph(
    "(4) In the absence of the Chairman of a Committee, Sub-Committee or a Divisional Committee at a meeting, the vice-chairman "
    "shall preside over the meeting, and if both the Chairman and Vice-Chairman are absent, the members present shall elect one "
    "of them present to preside over the meeting.", body))
story.append(SP())

# PART XV
story.append(Paragraph("PART XV – TRAFFIC WARDEN SERVICE", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>120.</b>&nbsp;&nbsp;&nbsp;(1) There is established a Traffic Warden Service (in this Act referred to as \"the Warden Service\").", body))
story.append(Paragraph("(2) The Warden Service shall consist of traffic wardens appointed from time to time under this Act.", body))
story.append(Paragraph(
    "(3) The Warden Service shall be a part of the Police Force and accordingly, references to the Police Force shall, subject "
    "to the provisions of this Act, include references to the Warden Service.", body))
story.append(Paragraph(
    "(4) Notwithstanding subsection (3), where any Act, whether passed before or after the commencement of this Act, requires "
    "police officers to discharge military duties, or confers any power on any person whether expressly or in general terms to "
    "require police officers to discharge those duties, that Act shall not, in the absence of express provision to the contrary, "
    "extend to traffic wardens.", body))
story.append(Paragraph(
    "(5) Traffic wardens shall be employed to perform functions normally undertaken by police officers in connection with the "
    "control and regulation of, or the enforcement of the law relating to, road traffic and shall, in that connection, act "
    "under the direction of the Police Force.", body))
story.append(Paragraph(
    "(6) Without prejudice to the generality of the provisions of subsections (1) - (5), a traffic warden shall deal primarily with:", body))
story.append(Paragraph("(a) the general control and direction of motor traffic on the highway;", body_indent))
story.append(Paragraph("(b) assisting pedestrians to cross the road; and", body_indent))
story.append(Paragraph("(c) controlling vehicles stopping or parking in unauthorised places.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>121.</b>&nbsp;&nbsp;&nbsp;(1) Notwithstanding anything to the contrary in any law, the Inspector-General of Police "
    "has power to appoint, promote, transfer, dismiss or exercise disciplinary control over traffic wardens.", body))
story.append(Paragraph(
    "(2) Subject to the provisions of this Act, a person may be recruited a traffic warden if he:", body))
story.append(Paragraph("(a) is not less than 18 and not more than 25 years of age;", body_indent))
story.append(Paragraph(
    "(b) is in possession of a minimum educational qualification of Senior Secondary School Certificate;", body_indent))
story.append(Paragraph(
    "(c) at least 167.64 centimetres and 162.56 centimetres tall respectively for the men and women;", body_indent))
story.append(Paragraph(
    "(d) in the case of men, has at least 86.36 centimetres chest measurement when fully expanded;", body_indent))
story.append(Paragraph("(e) is of good character and physically fit; and", body_indent))
story.append(Paragraph("(f) has signified his willingness to serve as a traffic warden.", body_indent))
story.append(Paragraph(
    "(3) The Police Service Commission on the recommendation of the Inspector-General of Police shall from time to time by "
    "notice published in the Federal Government Gazette, fix the maximum number of persons who may at any given time hold "
    "office under this section; and a person shall not be enlisted as a traffic warden if his enlistment would cause the number "
    "for the time being so fixed to be exceeded.", body))
story.append(Paragraph("(4) The Inspector-General of Police may-", body))
story.append(Paragraph(
    "(a) from time to time with the approval of the Police Service Commission, fix the maximum number of traffic wardens who "
    "may, at any time, hold appointments in any State;", body_indent))
story.append(Paragraph(
    "(b) at his own discretion, fix the maximum number of traffic wardens who may, at any time, hold any particular rank in "
    "the Warden Service in any State: and", body_indent))
story.append(Paragraph("(c) in either case, fix different numbers with respect to different States.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>122.</b>&nbsp;&nbsp;&nbsp;(1) A traffic warden on appointment, or if re-appointed for a further term, shall make and "
    "subscribe to the police declaration prescribed by the Oaths Act as modified under subsection (2).", body))
story.append(Paragraph(
    "(2) The police declaration prescribed by the Oaths Act is modified by substituting for the words:", body))
story.append(Paragraph(
    "(a) \"police officer\", wherever they occur, the words \"traffic warden\"; and", body_indent))
story.append(Paragraph(
    "(b) \"for the preservation of peace\" to the end of the declaration, the words, \"to discharge all duties of my office according to law\".", body_indent))
story.append(SP(0.5))

story.append(Paragraph("<b>123.</b>&nbsp;&nbsp;&nbsp;(1) A traffic warden appointed under this Act shall be:", body))
story.append(Paragraph(
    "(a) appointed to serve as a traffic warden for 35 years of service or 60 years of age whichever comes first; and", body_indent))
story.append(Paragraph("(b) pensionable only in the Police State Command in which he resides.", body_indent))
story.append(Paragraph(
    "(2) A traffic warden may, subject to satisfactory conduct and service, be re-appointed for further three years until the "
    "expiration of the tenth year of his appointment in the Warden Service, when he may elect to determine his appointment or "
    "elect that his service be allowed to continue until he is 55 years of age.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>124.</b>&nbsp;&nbsp;&nbsp;A traffic warden appointed under this Act shall, when on duty:", body))
story.append(Paragraph(
    "(a) have the powers, privileges and immunities of a police officer under any law relating to the regulation of road traffic; and", body_indent))
story.append(Paragraph(
    "(b) be in uniform within the Police State Command in which he is appointed to serve, but not elsewhere.", body_indent))
story.append(SP(0.5))

story.append(Paragraph("<b>125.</b>&nbsp;&nbsp;&nbsp;A traffic warden:", body))
story.append(Paragraph(
    "(a) on first appointment, shall be issued with a certificate of appointment in a form approved by the Inspector-General of Police; and", body_indent))
story.append(Paragraph(
    "(b) on the determination of that or any subsequent appointment whether by effluxion of time or under section 120 of this "
    "Act, shall in like manner be issued with a Certificate of Discharge.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>126.</b>&nbsp;&nbsp;&nbsp;A traffic warden shall have such rank as may be assigned to him by the Inspector-General "
    "of Police beyond the following grades:", body))
story.append(Paragraph("(a) Traffic Warden Grade III;", body_indent))
story.append(Paragraph("(b) Traffic Warden Grade II;", body_indent))
story.append(Paragraph("(c) Traffic Warden Grade I;", body_indent))
story.append(Paragraph("(d) Senior Traffic Warden II;", body_indent))
story.append(Paragraph("(e) Senior Traffic Warden I;", body_indent))
story.append(Paragraph("(f) Assistant Superintendent of Traffic II;", body_indent))
story.append(Paragraph("(g) Assistant Superintendent of Traffic I;", body_indent))
story.append(Paragraph("(h) Deputy Superintendent of Traffic.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>127.</b>&nbsp;&nbsp;&nbsp;(1) A traffic warden appointed under this Act may at any time give to any senior police "
    "officer under whom he is serving, notice in writing of his intention to resign his appointment on a date mentioned in "
    "the notice not being less than 28 days later than the date on which the notice is given.", body))
story.append(Paragraph(
    "(2) On receipt by the senior police officer of the notice referred to in subsection (1) of this section, the senior "
    "police officer shall immediately refer such notice to the Commissioner having control over him and the traffic warden and "
    "if the Commissioner consents to the notice having effect, the appointment of the traffic warden shall be terminated.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>128.</b>&nbsp;&nbsp;&nbsp;(1) In so far as the context so admits, but subject to the provisions of this Act, a traffic "
    "warden shall be subject to the provisions of the Police Regulations subsidiary to this Act, for purposes of discipline.", body))
story.append(Paragraph(
    "(2) In the application to Traffic Wardens of the Second Schedule to the Police Regulations, references to Constables, "
    "Corporals, Sergeants, Inspectors and Senior Police Officers shall include respectively references to Traffic Wardens "
    "Grade III-I and Senior Traffic Wardens Grade II-I and Superintendents of Traffic respectively.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>129.</b>&nbsp;&nbsp;&nbsp;(1) The Inspector-General of Police may provide, for use by the traffic wardens, such "
    "equipment as he considers necessary for the proper discharge of their duties under this Act.", body))
story.append(Paragraph(
    "(2) Any expenses incurred by the Inspector-General of Police under this section shall be defrayed out of the General "
    "Fund of the Police Force.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>130.</b>&nbsp;&nbsp;&nbsp;(1) A traffic warden is required to undergo a course of training at the Traffic Training "
    "School of a Police College for 12 weeks or such other or further period as the Inspector-General of Police may determine.", body))
story.append(Paragraph(
    "(2) A traffic warden shall, on appointment, be allocated a service number with the letters, \"TW\" and the service "
    "numbers of all traffic wardens employed under this Act shall appear on the register kept for that purpose by the "
    "Inspector-General of Police.", body))
story.append(Paragraph(
    "(3) A traffic warden to whom a service number has been allocated under subsection (2) shall wear his service number on "
    "the shoulder flaps of his uniform whenever he is on duty.", body))
story.append(SP())

# PART XVI
story.append(Paragraph("PART XVI - POLICE PUBLIC COMPLAINTS AND DISCIPLINE", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>131.</b>&nbsp;&nbsp;&nbsp;(1) The Inspector-General of Police shall establish a Police Complaints Response Unit (in "
    "this Act referred to as \"the Unit\") in the Force Headquarters, and each of the Police Commands in all the States of "
    "the Federation and the Federal Capital Territory.", body))
story.append(Paragraph(
    "(2) The Unit established under subsection (1) shall be under the Public Relations Section.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>132.</b>&nbsp;&nbsp;&nbsp;(1) The Unit shall consist of representatives of the Federal or State Intelligence Bureau, "
    "Police Provost Marshal and any other unit of the Police Force as the Inspector-General of Police considers fit.", body))
story.append(Paragraph(
    "(2) The Unit shall be headed by an officer not below the rank of a Chief Superintendent of Police.", body))
story.append(SP(0.5))

story.append(Paragraph("<b>133.</b>&nbsp;&nbsp;&nbsp;(1) The Unit shall receive:", body))
story.append(Paragraph("(a) complaint or information of police officers misconduct from the public; or", body_indent))
story.append(Paragraph("(b) complaint of police officers misconduct from other police members or authority.", body_indent))
story.append(Paragraph("(2) The Unit may receive:", body))
story.append(Paragraph(
    "(a) any complaint alleging that the conduct complained of resulted in the death of or serious injury or other gross human rights violations;", body_indent))
story.append(Paragraph("(b) any complaint showing that a police officer may have committed a criminal offence; or", body_indent))
story.append(Paragraph(
    "(c) any complaint which shows that a police officer is involved in an act constituting professional misconduct.", body_indent))
story.append(Paragraph("(3) The Unit shall monitor the investigations initiated by the Unit.", body))
story.append(Paragraph(
    "(4) While conducting investigation into any complaint by any member of the public against a police officer, the Nigeria "
    "Police Force shall afford the person against whom the complaint has been made opportunity to defend himself.", body))
story.append(Paragraph(
    "(5) Upon the conclusion of an investigation, the appropriate investigative unit shall make available a copy of its "
    "findings or investigation report to the Unit within 21 days from the day the complaint was made.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>134.</b>&nbsp;&nbsp;&nbsp;After investigation, the head of the Unit through the Force Public Relations Officer or "
    "Public Relations Officer of a State or the Federal Capital Territory shall forward the report and its recommendations to "
    "the Inspector-General or Commissioner of Police a State or the Federal Capital Territory who shall:", body))
story.append(Paragraph(
    "(a) send a copy of the investigation report and recommendations to the appropriate Police or oversight authority for "
    "proper disciplinary action if the investigations reveal that the offence committed is against discipline as specified in "
    "this Act and in the Police Regulations made under this Act; and", body_indent))
story.append(Paragraph(
    "(b) where it is discovered after investigations that the complainant knowingly gave false information against the police "
    "officer or should have reasonably known that the information is false, the complainant shall be tried according to relevant "
    "laws for the time being in force.", body_indent))
story.append(SP())

# PART XVII
story.append(Paragraph("PART XVII – MISCELLANEOUS PROVISIONS", part_heading))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>135.</b>&nbsp;&nbsp;&nbsp;The Police Force or other persons shall not, in the performance of his or its functions "
    "under this Act, regulations or standing orders made under to this Act, discriminate against any person on the basis of "
    "gender as provided under section 42 of the Constitution of the Federal Republic of Nigeria, 1999.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>136.</b>&nbsp;&nbsp;&nbsp;All the provisions of this Act shall extend to all persons who, at the commencement of this "
    "Act are serving in the Nigeria Police Force established by the Constitution of the Federal of Nigeria as if such persons "
    "had been appointed under this Act.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>137.</b>&nbsp;&nbsp;&nbsp;(1) A police officer who, on reasonable grounds, believes that an order given to him by a "
    "senior officer is unlawful, he:", body))
story.append(Paragraph("(a) is not bound to comply with the order; and", body_indent))
story.append(Paragraph(
    "(b) shall immediately make a report in such form as it is provided by the Police Service Commission for that purpose.", body_indent))
story.append(Paragraph(
    "(2) On the receipt of the report referred to in subsection (1), the Police Service Commission shall immediately inquire "
    "into the matter and may, where the inquiry reveals that the order was:", body))
story.append(Paragraph(
    "(a) lawful, take appropriate disciplinary action against the police officer for disobeying a lawful order; and", body_indent))
story.append(Paragraph(
    "(b) unlawful, take appropriate disciplinary action against the senior police officer for giving an unlawful order.", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>138.</b>&nbsp;&nbsp;&nbsp;(1) The Minister may make regulations on the recommendation of:", body))
story.append(Paragraph(
    "(a) the Inspector-General of Police, with respect to the policy, organisation and administration of the Police Force, "
    "including establishments and financial matters, other than pensions within the meaning of the Pensions Reform Act.", body_indent))
story.append(Paragraph(
    "(b) the Police Service Commission, with respect to appointments, promotions and disciplinary control of police officers "
    "as specified in the Constitution.", body_indent))
story.append(Paragraph("(2) The Minister shall regularly review the police regulations.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>139.</b>&nbsp;&nbsp;&nbsp;(1) The Police Act Cap P19 Laws of the Federation of Nigeria, 2004 is repealed.", body))
story.append(Paragraph(
    "(2) Subject to section 6 of the Interpretation Act (relating to the repeal of enactments), the repeal of the Act referred "
    "to under subsection (1) does not affect anything done or purported to have been done under it.", body))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>140.</b>&nbsp;&nbsp;&nbsp;(1) There are vested in the Police Force established under this Act, all assets, funds, "
    "resources and other moveable or immoveable property which immediately before the commencement of this Act were vested in "
    "the Police Force existing immediately before the commencement of this Act.", body))
story.append(Paragraph(
    "(2) All rights, interests, obligations and liabilities of the Police Force existing immediately before the commencement "
    "of this Act under any contract or instrument, or in law or in equity, are by virtue of this Act assigned to and vested "
    "in the Police Force established under this Act.", body))
story.append(Paragraph(
    "(3) Any contract or instrument referred to in subsection (2) has the same effect against or in favour of the Police Force "
    "established under this Act and shall be enforced as fully and effectively as if, instead of the Police Force existing "
    "immediately before the commencement of this Act, the Police Force established under this Act had been named in it or had been a party to it.", body))
story.append(Paragraph(
    "(4) Any proceeding or cause of action pending or existing immediately before the commencement of this Act in respect of "
    "any right, interest, obligation or liability of the Police Force existing immediately before the commencement of this Act "
    "may be continued, or as the case may require, be commenced and the determination of a court or tribunal or other authority "
    "or person may be enforced by or against the Police Force established under this Act to the same extent that the cause of "
    "action or determination might have been continued or commenced or enforced by or against the Police Force existing "
    "immediately before the commencement of this Act as if this Act had not been enacted.", body))
story.append(Paragraph(
    "(5) Subject to the provisions of this Act and to such directions as may be issued by the Police Service Commission, a "
    "person who immediately before the commencement of this Act held office in the Police Force existing before the "
    "commencement of this Act is deemed to have been transferred to the Police Force established under this Act on terms and "
    "conditions not less favourable than those obtaining immediately before the commencement of this Act and employment in "
    "the Police Force existing immediately before the commencement of this Act is deem to be service in the Police Force "
    "established under this Act for the purpose of pension.", body))
story.append(Paragraph(
    "(6) Any regulation, order, notice made or issued by or for the purpose of the Police Force existing immediately before "
    "the commencement of this Act are deemed, if not inconsistent with this Act, to have been made or issued by or for the "
    "purposes of the Police Force established under this Act and shall continue in force until revoked or amended, subject to "
    "such modifications as may, from time to time be applicable to the Police Force established under this Act.", body))
story.append(Paragraph(
    "(7) The Minister may if he thinks fit, within 12 months after the commencement of this Act, by notice published in the "
    "Federal Government Gazette, make additional transitional provisions for the better carrying out of the objectives of this section.", body))
story.append(SP(0.5))

story.append(Paragraph("<b>141.</b>&nbsp;&nbsp;&nbsp;In this Act:", body))
for term, definition in [
    ("\"Commissioner\"", "means a Commissioner of Police, a Deputy Commissioner of Police or an Assistant Commissioner of Police;"),
    ("\"Constable\"", "means any police officer below the rank of Corporal;"),
    ("\"Constitution\"", "means the Constitution of the Federal Republic of Nigeria, 1999 (as altered);"),
    ("\"court\"", "means any court established by any law in force in Nigeria;"),
    ("\"Criminal Justice Monitoring Committee\"", "refers to the Administration of Criminal Justice Monitoring Committee set up under section 469 of the Administration of Criminal Justice Act to ensure effective and efficient application of the Act, speedy dispensation of criminal matters and for related matters;"),
    ("\"functions\"", "includes duties;"),
    ("\"Inspector\"", "includes a Chief Inspector and an Inspector of Police;"),
    ("\"Minister\"", "means the Minister charged with responsibility over police matters;"),
    ("\"Ministry\"", "shall be construed accordingly;"),
    ("\"Non-Commissioned Officer\"", "means a Police Sergeant-Major, a Police Sergeant or a Police Corporal as the case may be;"),
    ("\"Police\"", "means the Police Force;"),
    ("\"Police Force\"", "means the Police Force established under section 3 of this Act;"),
    ("\"police officer\"", "means a member of the Nigerian Police;"),
    ("\"prosecuting officer\"", "means any person appointed by the Attorney-General of the Federation or of the States to prosecute crimes on their behalf and for the Nigeria Police;"),
    ("\"senior police officer\"", "means any police officer above the rank of a Cadet Assistant Superintendent of Police; and"),
    ("\"Superintendent of Police,\"", "includes a Chief Superintendent of Police, Superintendent of Police, a Deputy Superintendent of Police, and an Assistant Superintendent of Police."),
]:
    story.append(Paragraph(f"{term} {definition}", body_indent))
story.append(SP(0.5))

story.append(Paragraph(
    "<b>142.</b>&nbsp;&nbsp;&nbsp;This Act may be cited as the Nigeria Police Act, 2020.", body))
story.append(SP())

# SCHEDULE
story.append(PageBreak())
story.append(Paragraph("SCHEDULE", center_bold))
story.append(SP(0.5))
story.append(Paragraph("Section 3 (3)", ParagraphStyle("right_note", parent=styles["Normal"],
                                                         alignment=TA_CENTER, fontSize=9, italic=True)))
story.append(SP())
story.append(Paragraph(
    "Subject to section 215 (1) of the 1999 Constitution of the Federal Republic of Nigeria (as amended), "
    "the hierarchy of the Police shall consist of the following:", body))
story.append(SP(0.5))

ranks = [
    "(i) The Inspector-General of Police;",
    "(ii) Deputy Inspectors-General of Police;",
    "(iii) Assistant Inspectors-General of Police;",
    "(iv) Commissioners of Police;",
    "(v) Deputy Commissioners of Police;",
    "(vi) Assistant Commissioner of Police;",
    "(vii) Chief Superintendents of Police;",
    "(viii) Superintendents of Police;",
    "(ix) Deputy Superintendents of Police;",
    "(x) Assistant Superintendents of Police I;",
    "(xi) Assistant Superintendents of Police II;",
    "(xii) Cadet Assistant Superintendents of Police;",
    "(xiii) Chief Inspectors of Police;",
    "(xiv) Deputy Chief Inspectors of Police;",
    "(xv) Assistant Chief Inspectors of Police;",
    "(xvi) Principal Inspectors of Police;",
    "(xvii) Senior Inspectors of Police;",
    "(xviii) Inspectors of Police (Confirmed);",
    "(xix) Inspectors of Police (Unconfirmed);",
    "(xxi) Sergeant Majors;",
    "(xxii) Sergeants;",
    "(xxiii) Corporals;",
    "(xxiv) Constables I;",
    "(xxv) Constables II;",
    "(xxvi) Recruits; and",
    "(xxvii) such other officers as the Nigeria Police Council may, from time to time consider necessary for effective discharge of the functions of the Police.",
]
for r in ranks:
    story.append(Paragraph(r, body_indent))

story.append(SP(2))
story.append(HR())
story.append(SP())
story.append(Paragraph(
    "I CERTIFY, IN ACCORDANCE WITH SECTION 2 (1) OF THE ACTS AUTHENTICATION ACT CAP. A2, LAWS OF THE FEDERATION OF NIGERIA 2004, "
    "THAT THIS IS A TRUE COPY OF THIS BILL PASSED BY BOTH HOUSES OF THE NATIONAL ASSEMBLY.", body))
story.append(SP())
story.append(Paragraph("Arc. OJO OLATUNDE AMOS", center_bold))
story.append(Paragraph("Ag. CLERK TO THE NATIONAL ASSEMBLY", center_normal))
story.append(SP())
story.append(Paragraph("17th DAY OF AUGUST, 2020", center_normal))
story.append(SP(2))
story.append(Paragraph("I ASSENT", body))
story.append(SP())
story.append(Paragraph("MUHAMMADU BUHARI, GCFR", center_bold))
story.append(Paragraph("President of the Federal Republic of Nigeria", center_normal))
story.append(SP())
story.append(Paragraph("15th Day of September, 2020", center_normal))

# BUILD
doc.build(story)
print(f"PDF created: {OUTPUT}")
