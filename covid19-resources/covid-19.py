# Author: Anshik Bansal
# Feel free to use, copy, distribute or modify the Python Script, licensed under MIT License.
# Please ensure to provide proper credit for the same.

import streamlit as st
import pandas as pd
from csv import DictWriter
from datetime import datetime
import states_data

st.header('India Fights Covid-19')
st.write("Let's save our families and friends together!")
st.write("")
st.info("Click the TOP LEFT BAR / PANE to view the options.")
states = states_data.states_data()


def state_data(key):
    states_list = list(states.keys())
    state_selection = st.selectbox('States & Union Territories', options=states_list, key=key)

    district_lists = list(states[state_selection].keys())
    district_selection = st.selectbox('District', options=district_lists, key=key)

    cities = st.selectbox('Cities', options=list(states[state_selection][district_selection]), key=key)

    return state_selection, district_selection, cities

# 1. STATES IMPORTANT LINKS

st.write("---")
st.sidebar.subheader("Links & Helpline Number")
states_imp_links = {
    "": "",
    "National Links": {
        "Links": {
            "Cipla Med Access": "https://www.cipla.com/",
            "Dr. Reddy's COVID-19 Med Access": "https://readytofightcovid.in/",
            "Pan India Plasma Resources": "https://covidplasma.online/",
            "COVID-19 Resources Citizen's Compiled Data- 1": "https://docs.google.com/spreadsheets/d/1mrlaZg8jvduKcxvCWs"
                                                          "-phAdltgBmY3lTOFTgH4-SLzY/edit#gid=2047572279",
            "COVID-19 Resources Citizen's Compiled Data- 2": "https://docs.google.com/spreadsheets/d"
                                                             "/1fHiBtzxBC_3Q7I5SXr_GpNA4ivT73w4W4hjK6IkGDBY/edit#gid"
                                                             "=1482732175",
            "COVID-19 Resources Citizen's Compiled Data- 3": "https://shubhamkarjos.github.io/WebDev/Covid/Covid-Help"
                                                             "/main.html "

        },
        "COVID Helpline Number": "+911123978046",

    },
    "Andaman & Nicobar Islands": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "03192232102",
    },
    "Andhra Pradesh": {
        "Links": {
            "COVID-19 AP": "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/",
        },
        "COVID Helpline Number": "08662410978",
    },
    "Arunachal Pradesh": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "9436055743",
    },
    "Assam": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "6913347770",
    },
    "Bihar": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "104",
    },
    "Chandigarh": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "9779558282",
    },
    "Chhattisgarh": {
        "Links": {
            "COVID-19 Chattisgarh": "https://cg.nic.in/health/covid19/RTPBedAvailable.aspx",
        },
        "COVID Helpline Number": "07712235091, 104",
    },
    "Dadra & Nagar Haveli & Daman & Diu": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "104",
    },
    "Delhi": {
        "Links": {
            "COVID-19 Delhi": "https://coronabeds.jantasamvad.org/beds.html",
        },
        "COVID Helpline Number": "01122307145",
    },
    "Goa": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "104",
    },
    "Gujarat": {
        "Links": {
            "COVID-19 GandhiNagar": "https://vmc.gov.in/HospitalModuleGMC/BedDetails.aspx?HOSP_ID=HOS00041",
            "COVID-19 Vadodara": "https://vmc.gov.in/Covid19VadodaraApp/HospitalBedsDetails.aspx?tid=1",
            "COVID-19 Resources Citizen's Compiled Data- 1": "https://docs.google.com/spreadsheets/d"
                                                             "/1ZyrYsowjk6PdC9N5yKBxMslI7FypoeIqDvlAYrqprL8/edit#gid=0 "
        },
        "COVID Helpline Number": "104",
    },
    "Haryana": {
        "Links": {
            "COVID-19 Haryana": "https://coronaharyana.in/",
        },
        "COVID Helpline Number": "8558893911",
    },
    "Himachal Pradesh": {
        #         "Links": {
        #
        #         },
        "COVID Helpline Number": "104",
    },
    "Jammu & Kashmir": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "01912520982",
    },
    "Jharkhand": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "104",
    },
    "Karnataka": {
        "Links": {
            "COVID-19 Bangalore": "https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vS-ipQLaCHZ8id4t4_NHf1FM4vQmBGQrGHAPFzNzJeuuGKsY_It6Tdb0Un_bC9gmig5G2dVxlXHoaEp/pubhtml?gid=1381543057&single=true",
        },
        "COVID Helpline Number": "104",
    },
    "Kerala": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "04712552056",
    },
    "Ladakh": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "01982256462",
    },
    "Lakshadweep": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "104",
    },
    "Madhya Pradesh": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "07552527177",
    },
    "Maharashtra": {
        "Links": {
            "COVID-19 Nagpur": "http://nsscdcl.org/covidbeds/AvailableHospitals.jsp",
            "COVID-19 Panvel": "https://covidbedpanvel.in/HospitalInfo/showindex",
            "COVID-19 Pune": "https://covidpune.com/",
            "COVID-19 UlhasNagar": "https://umccovidbed.in/HospitalInfo/showindex",
            "COVID-19 Thane": "https://covidbedthane.in/HospitalInfo/showindex",
        },
        "COVID Helpline Number": "02026127394",
    },
    "Manipur": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "3852411668",
    },
    "Meghalaya": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "108",
    },
    "Mizoram": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "102",
    },
    "Nagaland": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "7005539653",
    },
    "Odisha (Orissa)": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "9439994859",
    },
    "Puducherry (Pondicherry)": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "104",
    },
    "Punjab": {
        "Links": {
            "COVID-19 Ludhiana": "http://hbmsludhiana.in/index_app_detail.php?type=all",
        }
    },
    "Rajasthan": {
        "Links": {
            "COVID-19 Rajasthan": "https://covidinfo.rajasthan.gov.in/covid-isolation-hospital.aspx",
        },
        "COVID Helpline Number": "01412225624",
    },
    "Sikkim": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "104",
    },
    "Tamil Nadu": {
        "Links": {
            "COVID-19 TN": "https://stopcorona.tn.gov.in/beds.php",
        },
        "COVID Helpline Number": "04429510500",
    },
    "Telangana": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "104",
    },
    "Tripura": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "03812315879",
    },
    "Uttarakhand (Uttaranchal)": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "104",
    },
    "Uttar Pradesh": {
        "Links": {
            "COVID-19 Lucknow": "https://docs.google.com/spreadsheets/d/1roxOi2_Uw4YBzLd5s8vC8cp6lbuM9016tWeWTcx2q5Y"
                                "/edit#gid=0 "
        },
        "COVID Helpline Number": "18001805145",
    },
    "West Bengal": {
        # "Links": {
        #
        # },
        "COVID Helpline Number": "3323412600",
    },
}

select_state = st.sidebar.selectbox("", list(states_imp_links.keys()))
st.write(states_imp_links[select_state])

st.sidebar.subheader("Offering or Required Assistance? ")
person_kind = st.sidebar.selectbox("", ["Please Select", "Providing Help!", "Need Your Help!"])

# 2. PROVIDING HELP

if person_kind == "Providing Help!":
    st.write("------------")
    st.write("Thank you for being a potential life saver.")
    st.write("Please provide correct information to the best of your knowledge.")
    st.write("")

    st.subheader("Volunteer for or Add a Lead:")
    requirement = st.selectbox("", ["Please Select", "Ambulance Services", "Child Care", "Home Visit",
                                    "Hospital Beds", "Medicine", "Oxygen Cylinders", "Plasma", "Others"])

    # 2.1 PROVIDING HELP: AMBULANCE SERVICES

    if requirement == "Ambulance Services":
        contact_person = st.text_input('Contact Person: ')
        st.subheader("Contact Number: Format: 9876543210, PLEASE DO NOT PREFIX +91.")
        contact_information = st.text_input('Contact Number: ')
        st.write("---")
        st.subheader("Provide Pickup Location: ")
        pickup_location_state, pickup_location_district, pickup_location_city = state_data(key="provider_pickup")
        st.write("---")
        st.subheader("Provide Drop Location: ")
        drop_location_state, drop_location_district, drop_location_city = state_data(key="provider_drop")
        verified_lead = st.selectbox("Verified: ", ["Yes", "No"])
        additional_notes = st.text_input('Additional Notes: ')
        created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        updated_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        submit_info = st.button('Submit the info!', key="provider_drop")
        if submit_info:
            if not contact_person or not contact_information:
                st.write("Please provide the necessary information."
                         " Contact Name & Mobile Number Info is necessary!")
            else:
                field_names = ["Contact Person", "Contact Mobile Number",
                               "Pickup: State", "Pickup: District", "Pickup: City",
                               "Drop: State", "Drop: District", "Drop: City", "Verified", "Additional Notes",
                               "Created Time", "Updated Time"]
                dict_data = {"Contact Person": contact_person,
                             "Contact Mobile Number": contact_information,
                             "Pickup: State": pickup_location_state,
                             "Pickup: District": pickup_location_district,
                             "Pickup: City": pickup_location_city,
                             "Drop: State": drop_location_state,
                             "Drop: District": drop_location_district,
                             "Drop: City": drop_location_city,
                             "Verified": verified_lead,
                             "Additional Notes": additional_notes,
                             "Created Time": created_time,
                             "Updated Time": updated_time
                             }

                with open('./ambulance_service_provider.csv', 'a') as f_object:
                    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                    dictwriter_object.writerow(dict_data)
                    f_object.close()
                    st.success('Information saved successfully. Thank you for being a helping hand at this time:)')

    # 2.2 PROVIDING HELP: CHILD CARE

    elif requirement == "Child Care":
        contact_person = st.text_input('Contact Person: ')
        contact_information = st.text_input('Contact Number: ')
        state, district, city = state_data("provider_child_care")
        verified_lead = st.selectbox("Verified: ", ["Yes", "No"])
        additional_notes = st.text_input('Additional Notes: ')
        created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        updated_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        submit_info = st.button('Submit the info!', key="provider_child_care")
        if submit_info:
            if not contact_person or not contact_information:
                st.write("Please provide the necessary information."
                         " Contact Name & Mobile Number Info is necessary!")

            else:
                field_names = ["Contact Person", "Contact Mobile Number",
                               "State", "District", "City", "Verified", "Additional Notes",
                               "Created Time", "Updated Time"]
                dict_data = {"Contact Person": contact_person,
                             "Contact Mobile Number": contact_information,
                             "State": state,
                             "District": district,
                             "City": city,
                             "Verified": verified_lead,
                             "Additional Notes": additional_notes,
                             "Created Time": created_time,
                             "Updated Time": updated_time
                             }
                with open('./child_care_provider.csv', 'a') as f_object:
                    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                    dictwriter_object.writerow(dict_data)
                    f_object.close()
                    st.success('Information saved successfully. Thank you for being a helping hand at this time:)')

    # 2.3 PROVIDING HELP: HOME VISIT

    elif requirement == "Home Visit":
        contact_person = st.text_input('Contact Person: ')
        contact_information = st.text_input('Enter Contact Number: ')
        state, district, city = state_data("provider_home_visit")
        verified_lead = st.selectbox("Verified: ", ["Yes", "No"])
        additional_notes = st.text_input('Additional Notes: ')
        created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        updated_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        submit_info = st.button('Submit the info!', key="provider_home_visit")
        if submit_info:
            if not contact_person or not contact_information:
                st.write("Please provide the necessary information."
                         " Contact Name & Mobile Number Info is necessary!")

            else:
                field_names = ["Contact Person", "Contact Mobile Number",
                               "State", "District", "City", "Verified", "Additional Notes",
                               "Created Time", "Updated Time"]
                dict_data = {"Contact Person": contact_person,
                             "Contact Mobile Number": contact_information,
                             "State": state,
                             "District": district,
                             "City": city,
                             "Verified": verified_lead,
                             "Additional Notes": additional_notes,
                             "Created Time": created_time,
                             "Updated Time": updated_time
                             }
                with open('./home_visit_provider.csv', 'a') as f_object:
                    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                    dictwriter_object.writerow(dict_data)
                    f_object.close()
                    st.success('Information saved successfully. Thank you for being a helping hand at this time:)')

    # 2.4 PROVIDING HELP: HOSPITAL BEDS

    elif requirement == "Hospital Beds":
        contact_person = st.text_input('Contact Name or Doctor Name: ')
        contact_information = st.text_input('Mobile Number: ')
        hospital_name = st.text_input('Hospital Name: ')
        hospital_address = st.text_input('Hospital Address: ')
        state, district, city = state_data("provider_hospital_beds")
        total_bed_count = st.text_input("Total Bed Count: ")
        oxygen_bed_count = st.text_input("Oxygen Bed Count: ")
        icu_bed_count = st.text_input("ICU Bed Count: ")
        ventilator_bed_count = st.text_input("Ventilator Bed Count: ")
        verified_lead = st.selectbox("Verified: ", ["Yes", "No"])
        additional_notes = st.text_input('Additional Notes: ')
        created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        updated_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        submit_info = st.button('Submit the info!', key="provider_hospital_beds")
        if submit_info:
            field_names = ["Contact Person", "Contact Mobile Number", "Hospital Name", "Hospital Address",
                           "State", "District", "City", "Total Bed Count",
                           "Oxygen Bed Count", "ICU Bed Count", "Ventilator Bed Count", "Verified", "Additional Notes",
                           "Created Time", "Updated Time"]
            dict_data = {"Contact Person": contact_person,
                         "Contact Mobile Number": contact_information,
                         "Hospital Name": hospital_name,
                         "Hospital Address": hospital_address,
                         "State": state,
                         "District": district,
                         "City": city,
                         "Total Bed Count": total_bed_count,
                         "Oxygen Bed Count": oxygen_bed_count,
                         "ICU Bed Count": icu_bed_count,
                         "Ventilator Bed Count": ventilator_bed_count,
                         "Verified": verified_lead,
                         "Additional Notes": additional_notes,
                         "Created Time": created_time,
                         "Updated Time": updated_time
                         }

            with open('./hospital_bed_provider.csv', 'a') as f_object:
                dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                dictwriter_object.writerow(dict_data)
                f_object.close()
                st.success('Information saved successfully. Thank you for being a helping hand at this time:)')

    # 2.5 PROVIDING HELP: MEDICINES

    elif requirement == "Medicine":
        contact_person = st.text_input('Distributor / Retailer Name: ')
        medicine_name = st.text_input('Medicine Name: ')
        state, district, city = state_data(key="provider_medicine")
        address = st.text_input('Distributor / Retailer Address: ')
        contact_information = st.text_input('Contact Mobile Number: ')
        verified_lead = st.selectbox("Verified: ", ["Yes", "No"])
        additional_notes = st.text_input('Additional Notes: ')
        created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        updated_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        submit_info = st.button('Submit the info!')
        if submit_info:
            if not contact_person or not address:
                st.write("Please provide the necessary information."
                         " Distributor / Retailer Name and Address Info is necessary!")
            else:
                field_names = ["Distributor Name", "Medicine Name",
                               "State", "District", "City", "Address", "Contact Number", "Verified", "Additional Notes",
                               "Created Time", "Updated Time"]
                dict_data = {"Distributor Name": contact_person,
                             "Medicine Name": medicine_name,
                             "State": state,
                             "District": district,
                             "City": city,
                             "Address": address,
                             "Contact Number": contact_information,
                             "Verified": verified_lead,
                             "Additional Notes": additional_notes,
                             "Created Time": created_time,
                             "Updated Time": updated_time
                             }

                with open('./medicines_provider.csv', 'a') as f_object:
                    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                    dictwriter_object.writerow(dict_data)
                    f_object.close()
                    st.success('Information saved successfully. Thank you for being a helping hand at this time:)')

    # 2.6 PROVIDING HELP: OXYGEN CYLINDERS

    elif requirement == "Oxygen Cylinders":
        contact_person = st.text_input('Contact Name: ')
        contact_information = st.text_input('Contact Mobile Number: ')
        just_refill = st.selectbox("Just refilling?", ["Yes", "No"])
        start_timings = st.time_input('Start Timing: ')
        end_timings = st.time_input('End Timing: ')
        availability_for = st.selectbox('Availability for', ["Home", "Hospitals", "Home & Hospitals"])
        address = st.text_input('Address: ')
        state, district, city = state_data(key="provider_oxygen_cylinders")
        verified_lead = st.selectbox("Verified: ", ["Yes", "No"])
        additional_notes = st.text_input('Additional Notes: ')
        created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        updated_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        submit_info = st.button('Submit the info!')

        if submit_info:
            if not contact_person or not contact_information:
                st.write("Please provide the necessary information so that we can help together!"
                         " Contact Name & Mobile Number Info is necessary!")
            else:
                field_names = ["Contact Person", "Contact Mobile Number", "Just Refill", "Start Timings", "End Timings",
                               "Availability for", "Address", "State", "District", "City", "Verified",
                               "Additional Notes", "Created Time", "Updated Time"]
                dict_data = {"Contact Person": contact_person,
                             "Contact Mobile Number": contact_information,
                             "Just Refill": just_refill,
                             "Start Timings": start_timings,
                             "End Timings": end_timings,
                             "Availability for": availability_for,
                             "Address": address,
                             "State": state,
                             "District": district,
                             "City": city,
                             "Verified": verified_lead,
                             "Additional Notes": additional_notes,
                             "Created Time": created_time,
                             "Updated Time": updated_time
                             }
                with open('./oxygen_cylinders_provider.csv', 'a') as f_object:
                    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                    dictwriter_object.writerow(dict_data)
                    f_object.close()
                    st.success('Information saved successfully. Thank you for being a helping hand at this time:)')

    # 2.7 PROVIDING HELP: PLASMA

    elif requirement == "Plasma":
        contact_person = st.text_input('Donor Name: ')
        contact_information = st.text_input('Donor Contact Number: ')
        contact_age = st.text_input("Donor Age: ")
        blood_group = st.selectbox('Patient Blood Group: ', ['Please Select', 'A+', 'A-', 'B+', 'B-', 'AB+',
                                                             'AB-', 'O+', 'O-', 'Bombay Blood Group'])
        recovered_date = st.date_input('Enter the date of recovery: ')
        state, district, city = state_data(key="provider_plasma")
        donated_before = st.selectbox("Have you donated it before?", ["Yes", "No"])
        if donated_before == "Yes":
            last_donated_date = st.date_input("Last Donated Date: ")
        else:
            last_donated_date = ""
        antibodies_test = st.selectbox("Tested for antibodies yet?", ["Yes", "No"])
        medical_issues = st.text_input("Any chronic disease such as high B.P., Diabetes etc.: ")
        verified_lead = st.selectbox("Verified: ", ["Yes", "No"])
        additional_notes = st.text_input('Additional Notes: ')
        created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        updated_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        submit_info = st.button('Submit the info!', key="provider_plasma")
        if submit_info:
            if not contact_person or not contact_information or not blood_group or not contact_age \
                    or not recovered_date or not donated_before:
                st.write("Please provide the necessary information so that we can help together!"
                         " Donor Name, Mobile Number, Age, Blood Group, Recovered Date, "
                         "and Donated Before Info is necessary!")
            else:
                field_names = ["Donor Name", "Donor Contact Number",
                               "Donor Age", "Donor Blood Group", "Recovered Date",
                               "State", "District", "City", "Donated Before", "Last Donated Date",
                               "Antibodies Test", "Medical Issues", "Verified", "Additional Notes",
                               "Created Time", "Updated Time"]
                dict_data = {"Donor Name": contact_person,
                             "Donor Contact Number": contact_information,
                             "Donor Age": contact_age,
                             "Donor Blood Group": blood_group,
                             "Recovered Date": recovered_date,
                             "State": state,
                             "District": district,
                             "City": city,
                             "Donated Before": donated_before,
                             "Last Donated Date": last_donated_date,
                             "Antibodies Test": antibodies_test,
                             "Medical Issues": medical_issues,
                             "Verified": verified_lead,
                             "Additional Notes": additional_notes,
                             "Created Time": created_time,
                             "Updated Time": updated_time
                             }
                with open('./plasma_provider.csv', 'a') as f_object:
                    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                    dictwriter_object.writerow(dict_data)
                    f_object.close()
                    st.success('Information saved successfully. Thank you for being a helping hand at this time:)')

    # 2.8 PROVIDING HELP: OTHERS

    elif requirement == "Others":
        text = st.text_input('Write others: ')
        verified_lead = st.selectbox("Verified: ", ["Yes", "No"])
        created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        updated_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        submit_info = st.button('Submit the info!', key="provider_others")
        if submit_info:
            field_names = ["Text", "Verified",
                           "Created Time", "Updated Time"]
            dict_data = {"Text": text,
                         "Verified": verified_lead,
                         "Created Time": created_time,
                         "Updated Time": updated_time}

            with open('./others_service_provider.csv', 'a') as f_object:
                dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                dictwriter_object.writerow(dict_data)
                f_object.close()
                st.success('Information saved successfully. Thank you for being a helping hand at this time:)')

# 3. NEED ASSISTANCE

elif person_kind == "Need Your Help!":
    st.write("------------")
    st.write("I'm trying my best to keep the webpage updated. Kindly please share with others so more data and "
             "verified leads can be collected and the resources be made available to the needful people.")

    requirement = st.selectbox("Need List", ["Ambulance Services", "Child Care", "Home Visit",
                                             "Hospital Beds", "Medicine", "Oxygen Cylinders", "Plasma", "Others"])

    # 3.1 ASSISTANCE: AMBULANCE SERVICES / HOSPITAL BED / PLASMA

    if requirement == "Ambulance Services" or requirement == "Hospital Beds" or requirement == "Plasma" \
            or requirement == "Oxygen Cylinders":
        patient_name = st.text_input('Patient Name: ')
        contact_information = st.text_input('Patient Mobile Number: ')
        patient_age = st.text_input('Patient Age: ')
        patient_sex = st.selectbox('Patient Sex: ', ['Male', 'Female', 'Transgender'])
        patient_condition = st.selectbox('Patient Condition: ', ['Stable', 'SOS'])
        assistance_for = st.selectbox("Assistance For: ", ["Ambulance Services", "Hospital Beds", "Oxygen Cylinder",
                                                           "Oxygen Cylinder Refill", "Plasma"])
        if assistance_for == "Ambulance Services":
            facilities = st.selectbox("Facilities: ", ["Normal", "Oxygen without AC", "Oxygen with AC", "Ventilator"])
        else:
            facilities = ""
        patient_blood_group = st.selectbox('Patient Blood Group: ', ['Please Select', 'A+', 'A-', 'B+', 'B-', 'AB+',
                                                                     'AB-', 'O+', 'O-', 'Bombay Blood Group'])
        if assistance_for == "Hospital Beds":
            bed_type = st.selectbox("Bed Type: ", ["Without Oxygen", "With Oxygen", "Ventilalor Bed"])
        else:
            bed_type = ""
        patient_oxygen_level = st.text_input("Patient Oxygen Level")
        state, district, city = state_data(key="assist_ambulance")
        address = st.text_input('Patient Address: ')
        additional_notes = st.text_input('Additional Notes: ')
        status = st.selectbox("Status", ["", "Resolved"])
        created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        updated_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        submit_info = st.button('Submit the info!')
        if submit_info:
            if not patient_name or not contact_information or not assistance_for:
                st.write("Please provide the necessary information."
                         " Patient Name, Mobile Number and Assistance For Info is necessary!")
            else:
                field_names = ["Patient Name", "Patient Mobile Number", "Patient Age", "Patient Sex", "Patient Condition",
                               "Assistance For", "Facilities", "Bed Type", "Patient Blood Group", "Patient Oxygen Level",
                               "State", "District", "City", "Address", "Additional Notes", "Status",
                               "Created Time", "Updated Time"]
                dict_data = {"Patient Name": patient_name,
                             "Patient Mobile Number": contact_information,
                             "Patient Age": patient_age,
                             "Patient Sex": patient_sex,
                             "Patient Condition": patient_condition,
                             "Assistance For": assistance_for,
                             "Facilities": facilities,
                             "Bed Type": bed_type,
                             "Patient Blood Group": patient_blood_group,
                             "Patient Oxygen Level": patient_oxygen_level,
                             "State": state,
                             "District": district,
                             "City": city,
                             "Address": address,
                             "Additional Notes": additional_notes,
                             "Status": status,
                             "Created Time": created_time,
                             "Updated Time": updated_time
                             }

                with open('./critical_assistance.csv', 'a') as f_object:
                    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                    dictwriter_object.writerow(dict_data)
                    f_object.close()
                    st.success('Information saved successfully. Please keep rechecking the page:)')

    # 3.2 ASSISTANCE: MEDICINE

    elif requirement == "Medicine":
        state = list(state_data(key="medicine_assistance"))
        df = pd.read_csv("./medicines_provider.csv")
        state_retailers_data = df[df["State"] == state[0]]

        st.table(state_retailers_data)
        # for iterate in range(retailers_count[0]):
        #     retailer_data = state_retailers_data.iloc[iterate, :]
        #     data_to_df = pd.DataFrame(retailer_data, columns=[0])
        #     retailer_info = data_to_df.dropna()
        #     st.write(retailer_info)

    # 3.3 ASSISTANCE: HOME VISIT / CHILD CARE

    elif requirement == "Home Visit" or requirement == "Child Care":
        contact_person = st.text_input('Patient Name: ')
        contact_information = st.text_input('Patient Mobile Number: ')
        patient_age = st.text_input('Patient Age: ')
        patient_sex = st.selectbox('Patient Sex: ', ['Male', 'Female', 'Transgender'])
        patient_condition = st.selectbox('Patient Condition: ', ['Stable', 'SOS'])
        assistance_for = st.selectbox("Assistance For: ", ["Home Visit", "Child Care"])
        state, district, city = state_data(key="assist_home_visit")
        address = st.text_input('Patient Address: ')
        additional_notes = st.text_input('Additional Notes: ')
        status = st.selectbox("Status", ["", "Resolved"])
        created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        updated_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        submit_info = st.button('Submit the info!')
        if submit_info:
            if not contact_person or not contact_information or not assistance_for:
                st.write("Please provide the necessary information."
                         " Patient Name, Mobile Number and Assistance For Info is necessary!")
            else:
                field_names = ["Patient Name", "Patient Mobile Number", "Patient Age", "Patient Sex", "Patient Condition",
                               "Assistance For", "State", "District", "City", "Address", "Additional Notes", "Status",
                               "Created Time", "Updated Time"]
                dict_data = {"Patient Name": contact_person,
                             "Patient Mobile Number": contact_information,
                             "Patient Age": patient_age,
                             "Patient Sex": patient_sex,
                             "Patient Condition": patient_condition,
                             "Assistance For": assistance_for,
                             "State": state,
                             "District": district,
                             "City": city,
                             "Address": address,
                             "Additional Notes": additional_notes,
                             "Status": status,
                             "Created Time": created_time,
                             "Updated Time": updated_time
                             }

                with open('./home_personal_assistance.csv', 'a') as f_object:
                    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                    dictwriter_object.writerow(dict_data)
                    f_object.close()
                    st.success('Information saved successfully. Please keep rechecking the page:)')

    # 2.4 ASSISTANCE: OTHERS

    elif requirement == "Others":
        text = st.text_input('Write others: ')
        status = st.selectbox("Status", ["", "Resolved"])
        created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        updated_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        submit_info = st.button('Submit the info!')
        if submit_info:
            field_names = ["Text", "Status"
                                   "Created Time", "Updated Time"]
            dict_data = {"Text": text,
                         "Status": status,
                         "Created Time": created_time,
                         "Updated Time": updated_time}

            with open('./others_service_assistance.csv', 'a') as f_object:
                dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                dictwriter_object.writerow(dict_data)
                f_object.close()
                st.success('Information saved successfully. Please keep rechecking the page:)')

# 4. UPDATE THE DATA

st.sidebar.subheader("Update the Data!")

data_type = st.sidebar.selectbox("", ["Please Select",
                                      "Need Assistance: Ambulance Services", "Providing Assistance: Ambulance Services",
                                      "Need Assistance: Child Care", "Providing Assistance: Child Care",
                                      "Need Assistance: Home Visit", "Providing Assistance: Home Visit",
                                      "Need Assistance: Hospital Beds", "Providing Assistance: Hospital Beds",
                                      "Providing Assistance: Medicine",
                                      "Need Assistance: Oxygen Cylinders", "Providing Assistance: Oxygen Cylinders",
                                      "Need Assistance: Plasma", "Providing Assistance: Plasma",
                                      ])

# 4.1 UPDATE: NEED ASSISTANCE: HOME VISIT AND CHILD CARE

if data_type == "Need Assistance: Home Visit" or data_type == "Need Assistance: Child Care":
    df = pd.read_csv("./home_personal_assistance.csv")
    patient_name = st.text_input('Patient Name: ')
    patient_mobile_number = st.text_input('Patient Mobile Number: ')
    assistance_for = st.selectbox("Assistance For: ", ["Home Visit", "Child Care"])
    if patient_name and patient_mobile_number and assistance_for:
        patient_mobile_number = int(patient_mobile_number)
        field_names = ["Patient Name", "Patient Mobile Number", "Patient Age", "Patient Sex", "Patient Condition",
                       "Assistance For", "State", "District", "City", "Address", "Additional Notes", "Status"]
        select_field = st.selectbox("Select Info to be updated:", field_names)
        updated_data = st.text_input("Updated Info: ")
        df.loc[(df["Patient Name"] == patient_name) & (df["Patient Mobile Number"] == patient_mobile_number)
               & (df["Assistance For"] == assistance_for), select_field] = updated_data
        df.loc[(df["Patient Name"] == patient_name) & (df["Patient Mobile Number"] == patient_mobile_number)
               & (df["Assistance For"] == assistance_for), "Updated Time"] = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S")
        st.subheader("Verify the details below before submitting the updated data:")

        submit_info = st.button('Submit the info!')
        if submit_info:
            df.to_csv("./home_personal_assistance.csv", index=False)
            st.success('Information updated successfully. Please keep rechecking the page:)')


# 4.2 UPDATE: NEED ASSISTANCE: AMBULANCE SERVICES, HOSPITAL BEDS, PLASMA, OXYGEN CYLINDERS

elif data_type == "Need Assistance: Ambulance Services" or data_type == "Need Assistance: Hospital Beds" or \
        data_type == "Need Assistance: Plasma" or data_type == "Need Assistance: Oxygen Cylinders":
    df = pd.read_csv("./critical_assistance.csv")
    patient_name = st.text_input('Patient Name: ', key="Patient Name")
    contact_information = st.text_input('Patient Mobile Number: ', key="Contact Info")
    assistance_option = ["Ambulance Services", "Hospital Beds", "Oxygen Cylinder",
                         "Oxygen Cylinder Refill", "Plasma"]
    assistance = st.selectbox('Assistance For', options=assistance_option, key="Patient Assistance")
    if patient_name and contact_information and assistance:
        contact_information = int(contact_information)
        fields = ["Patient Name", "Patient Mobile Number", "Patient Age", "Patient Sex", "Patient Condition",
                  "Assistance For", "Facilities", "Bed Type", "Patient Blood Group", "Patient Oxygen Level",
                  "State", "District", "City", "Address", "Additional Notes", "Status"]
        select_field = st.selectbox("Select Info to be updated:", fields)
        updated_data = st.text_input("Updated Info: ")
        df.loc[(df["Patient Name"] == patient_name) & (df["Patient Mobile Number"] == contact_information)
               & (df["Assistance For"] == assistance), select_field] = updated_data
        df.loc[(df["Patient Name"] == patient_name) & (df["Patient Mobile Number"] == contact_information)
               & (df["Assistance For"] == assistance), "Updated Time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        submit_info = st.button('Submit the info!')
        if submit_info:
            df.to_csv("./critical_assistance.csv", index=False)
            st.success('Information updated successfully. Please keep rechecking the page:)')

# 4.3 UPDATE: VOLUNTEER: CHILD CARE

elif data_type == "Providing Assistance: Child Care":
    df = pd.read_csv("./child_care_provider.csv")
    contact_person = st.text_input('Enter Contact Name: ')
    contact_information = st.text_input('Contact Number: ')
    if contact_person and contact_information:
        contact_information = int(contact_information)
        fields = ["Contact Person", "Contact Mobile Number",
                  "State", "District", "City", "Verified", "Additional Notes",
                  ]
        select_field = st.selectbox("Select Info to be updated:", field_names)
        updated_data = st.text_input("Updated Info: ")
        df.loc[(df["Contact Person"] == contact_person) & (df["Contact Mobile Number"] == contact_information)
        , select_field] = updated_data
        df.loc[(df["Contact Person"] == contact_person) & (df["Contact Mobile Number"] == contact_information)
        , "Updated Time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        submit_info = st.button('Submit the info!')
        if submit_info:
            df.to_csv("./child_care_provider.csv", index=False)
            st.success('Information updated successfully. :)')

# 4.4 UPDATE: VOLUNTEER: AMBULANCE SERVICE PROVIDER

elif data_type == "Providing Assistance: Ambulance Services":
    df = pd.read_csv("./ambulance_service_provider.csv")
    contact_person = st.text_input('Enter Contact Name: ')
    contact_information = st.text_input('Contact Mobile Number: ')
    if contact_person and contact_information:
        contact_information = int(contact_information)
        field_names = ["Contact Person", "Contact Mobile Number",
                       "Pickup: State", "Pickup: District", "Pickup: City",
                       "Drop: State", "Drop: District", "Drop: City", "Verified", "Additional Notes",
                       ]
        select_field = st.selectbox("Select Info to be updated:", field_names)
        updated_data = st.text_input("Updated Info: ")
        df.loc[(df["Contact Person"] == contact_person) & (df["Contact Mobile Number"] == contact_information)
        , select_field] = updated_data
        df.loc[(df["Contact Person"] == contact_person) & (df["Contact Mobile Number"] == contact_information)
        , "Updated Time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        submit_info = st.button('Submit the info!')
        if submit_info:
            df.to_csv("./ambulance_service_provider.csv", index=False)
            st.success('Information updated successfully. :)')

    # 3.5 UPDATE: VOLUNTEER: HOSPITAL BED PROVIDER

    elif data_type == "Providing Assistance: Hospital Beds":
        df = pd.read_csv("./hospital_bed_provider.csv")
        hospital_name = st.text_input('Hospital Name: ')
        hospital_address = st.text_input('Hospital Address: ')
        if hospital_name and hospital_address:
            field_names = ["Contact Person", "Contact Mobile Number", "Hospital Name", "Hospital Address",
                           "State", "District", "City", "Total Bed Count",
                           "Oxygen Bed Count", "ICU Bed Count", "Ventilator Bed Count", "Verified", "Additional Notes",
                           ]
            select_field = st.selectbox("Select Info to be updated:", field_names)
            updated_data = st.text_input("Updated Info: ")
            df.loc[(df["Hospital Name"] == hospital_name) & (df["Hospital Address"] == hospital_address)
            , select_field] = updated_data
            df.loc[(df["Hospital Name"] == hospital_name) & (df["Hospital Address"] == hospital_address)
            , "Updated Time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            submit_info = st.button('Submit the info!')
            if submit_info:
                df.to_csv("./hospital_bed_provider.csv")
                st.success('Information updated successfully. :)')

    st.write("----")

# 4.5 UPDATE: VOLUNTEER: MEDICINE PROVIDER

elif data_type == "Providing Assistance: Medicine":
    df = pd.read_csv("./medicines_provider.csv")
    contact_person = st.text_input('Distributor / Retailer Name: ')
    address = st.text_input('Distributor / Retailer Address:')
    if contact_person and address:
        field_names = ["Distributor Name", "Medicine Name",
                       "State", "District", "City", "Address", "Contact Number", "Verified", "Additional Notes",
                       ]
        select_field = st.selectbox("Select Info to be updated:", field_names)
        updated_data = st.text_input("Updated Info: ")
        df.loc[(df["Distributor Name"] == contact_person) & (df["Address"] == address)
        , select_field] = updated_data
        df.loc[(df["Distributor Name"] == contact_person) & (df["Address"] == address)
        , "Updated Time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        submit_info = st.button('Submit the info!')
        if submit_info:
            df.to_csv("./medicines_provider.csv", index=False)
            st.success('Information updated successfully. :)')

# 4.6 UPDATE: VOLUNTEER: OXYGEN CYLINDERS PROVIDER

elif data_type == "Providing Assistance: Oxygen Cylinders":
    df = pd.read_csv("./oxygen_cylinders_provider.csv")
    contact_person = st.text_input('Contact Name: ')
    contact_information = st.text_input('Contact Mobile Number:')
    if contact_person and contact_information:
        field_names = ["Contact Person", "Contact Mobile Number", "Just Refill", "Start Timings", "End Timings",
                       "Availability for", "Address", "State", "District", "City", "Verified",
                       "Additional Notes"]
        select_field = st.selectbox("Select Info to be updated:", field_names)
        updated_data = st.text_input("Updated Info: ")
        df.loc[(df["Contact Person"] == contact_person) & (df["Contact Mobile Number"] == contact_information)
        , select_field] = updated_data
        df.loc[(df["Contact Person"] == contact_person) & (df["Contact Mobile Number"] == contact_information)
        , "Updated Time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        submit_info = st.button('Submit the info!')
        if submit_info:
            df.to_csv("./oxygen_cylinders_provider.csv", index=False)
            st.success('Information updated successfully. :)')

# 4.6 UPDATE: VOLUNTEER: PLASMA PROVIDER

elif data_type == "Providing Assistance: Plasma":
    df = pd.read_csv("./plasma_provider.csv")
    contact_person = st.text_input('Donor Name: ')
    contact_information = st.text_input('Donor Contact Number: ')
    if contact_person and contact_information:
        field_names = ["Donor Name", "Donor Contact Number",
                       "Donor Age", "Donor Blood Group", "Recovered Date",
                       "State", "District", "City", "Donated Before", "Last Donated Date",
                       "Antibodies Test", "Medical Issues", "Verified", "Additional Notes",
                       ]
        select_field = st.selectbox("Select Info to be updated:", field_names)
        updated_data = st.text_input("Updated Info: ")
        df.loc[(df["Donor Name"] == contact_person) & (df["Donor Contact Number"] == contact_information)
        , select_field] = updated_data
        df.loc[(df["Donor Name"] == contact_person) & (df["Donor Contact Number"] == contact_information)
        , "Updated Time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        submit_info = st.button('Submit the info!')
        if submit_info:
            df.to_csv("./plasma_provider.csv", index=False)
            st.success('Information updated successfully. :)')

# 4.7 UPDATE: VOLUNTEER: HOME VISIT PROVIDER

elif data_type == "Providing Assistance: Home Visit":
    df = pd.read_csv("./home_visit_provider.csv")
    contact_person = st.text_input('Contact Person: ')
    contact_information = st.text_input('Enter Contact Number: ')
    if contact_person and contact_information:
        field_names = ["Contact Person", "Contact Mobile Number",
                               "State", "District", "City", "Verified", "Additional Notes",
                               ]
        select_field = st.selectbox("Select Info to be updated:", field_names)
        updated_data = st.text_input("Updated Info: ")
        df.loc[(df["Contact Person"] == contact_person) & (df["Contact Mobile Number"] == contact_information)
        , select_field] = updated_data
        df.loc[(df["Contact Person"] == contact_person) & (df["Contact Mobile Number"] == contact_information)
        , "Updated Time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        submit_info = st.button('Submit the info!')
        if submit_info:
            df.to_csv("./home_visit_provider.csv", index=False)
            st.success('Information updated successfully. :)')

# 5. TWITTER SEARCH FOR COVID-19

st.sidebar.subheader("Twitter Search for Covid-19")
twitter_search = st.sidebar.checkbox("Generate Link")
if twitter_search:
    st.write("---")
    st.subheader("City Name")
    city = st.text_input("", "Ghaziabad")
    st.subheader("Show Posts with #verified")
    verified = st.selectbox("", ["Yes", "No"])
    if verified == "Yes":
        verified = "verified+"
    else:
        verified = ""

    st.subheader("Specify the Need [Multi-Select Option]")

    required = {
        "Bed": "bed+OR+beds",
        "Ventilator": "ventilator+OR+ventilators",
        "Oxygen": "oxygen",
        "ICU": "icu",
        "Test": "testing+OR+test+tests",
        "Remdesivir": "remdesivir",
        "Dexamethasone": "dexamethasone",
        "Tusq Dx": "tusq+OR+tusq+dx+OR+tusqdx",
        "Favipiravir": "favipiravir",
        "Tocilizumab": "tocilizumab",
        "Fabiflu": "fabiflu",
        "Plasma": "plasma",
        "Food": "food+OR+tiffin+OR+lunch"
    }

    multi_check = st.multiselect('', list(required.keys()))
    st.subheader("Additional Keyword, if any: ")
    other_keyword = st.text_input("")

    link_1 = ""
    for iterate, check in enumerate(multi_check):
        if iterate == 0:
            link_1 += required[check]
        else:
            link_1 += f"+{required[check]}"

    st.subheader('Include the posts with #not-verified, #needed [BY DEFAULT- EXCLUDED]')
    exclude_check = st.selectbox("", ["Select", "No"])
    if exclude_check == "No":
        link_2 = ''
    else:
        link_2 = "+-%22not+verified+-%22needed+-%22unverified+-%22required+-%22require+-%22nneed+-%22requirement"

    link_3 = f"+{other_keyword}"

    link = f"https://twitter.com/search?q={verified}{city}+%28{link_1}{link_3}%29{link_2}&f=live"

    link_submit_info = st.button('Generate and Copy the Twitter link here!', key="link_generator")
    if link_submit_info:
        copy_link = pd.DataFrame([link])
        copy_link.to_clipboard(index=False, header=False)
        st.code(link)

# 5. IMPORTANT

st.sidebar.subheader("Important!")
sos_patient = st.sidebar.checkbox("SOS Patients")
hosp_list = st.sidebar.checkbox("View Hospitals")
medicine_list = st.sidebar.checkbox("Medicine Distributors")

if medicine_list:
    # state_list = list(state_data(key="medicine_assistance"))
    # state_dist_data = df[df["State"] == state_list[0]]
    state_list = st.selectbox("", list(states.keys()))
    df = pd.read_csv("./medicines_provider.csv")
    state_dist_data = df[df["State"] == state_list]

    count = state_dist_data.shape[0]
    for i in range(count):
        state_med_store_raw = state_dist_data.iloc[i, :]
        state_med_store_df = pd.DataFrame(state_med_store_raw)
        state_med_store = state_med_store_df.dropna()
        st.write(state_med_store)

if sos_patient:
    patients_data = pd.read_csv("./critical_assistance.csv")

    count = patients_data.shape[0]
    for i in range(count):
        patients_data_raw = patients_data.iloc[i, :]
        patients_data_df = pd.DataFrame(patients_data)
        patient_data = patients_data.dropna()
        st.write(patient_data)

if hosp_list:

    hospital_data = pd.read_csv("./hospital_bed_provider.csv")
    if hospital_data.loc[hospital_data["District"] == "Select the District"].shape[0] > 0:
        hospital_data.loc[(hospital_data["District"] == "Select the District"), "Select the District"] = "nan"
        hospital_data.to_csv("./hospital_bed_provider.csv", index=False)
    if hospital_data.loc[hospital_data["City"] == "Select the City"].shape[0] > 0:
        hospital_data.loc[(hospital_data["City"] == "Select the City"), "Select the City"] = "nan"
        hospital_data.to_csv("./hospital_bed_provider.csv", index=False)

    count = hospital_data.shape[0]
    for i in range(count):
        hospital_data_raw = hospital_data.iloc[i, :]
        hospital_data_df = pd.DataFrame(hospital_data_raw)
        hosp_data = hospital_data.dropna()
        st.write(hosp_data)

# 7. REPORT AN ERROR

st.sidebar.subheader("Found any glitches, inform!")
report_error = st.sidebar.checkbox("Report an Error!")
if report_error:
    st.subheader("Please try to be detailed and more precise..")
    text = st.text_input("", "Example: I've discovered a glitch..")
    submit_info = st.button('Submit the info!', key="ReportAnError")
    if submit_info:
        field_names = ["Text"]
        dict_data = {"Text": text}

        with open('./report_an_error.csv', 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(dict_data)
            f_object.close()
            st.success('Information saved successfully. Thank you:)')

st.write("---")

st.markdown('Designed & Developed by <span style= "color:red">@anshik1998</span> '
            '<br/>Connect with me at: '
            '<a href="https://www.linkedin.com/in/anshik1998">LinkedIn</a>, '
            ' <a href="https://www.instagram.com/anshik1998">Instagram</a> .<br/>'
            'An Open Source Initiative for the people of our motherland. :)', unsafe_allow_html=True)
st.markdown("If any concern, shoot me a mail at: anshik1998@gmail.com, please do not spam.")