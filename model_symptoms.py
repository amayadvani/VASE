# possible symptoms that the user can check mark
symptoms_database = [
  "Cough", "Sore throat", "Headache", "Fever", "Muscle pain", "Stomach ache",
  "Congested nose", "Runny nose", "Painful coughing", "Swollen mouth",
  "Swollen face", "Pimples", "Sneezing", "Vomiting", "Fatigue", "Sore Throat",
  "Itchy Eyes", "Watery Eyes", "Mucus", "Ear Pain", "Increased heart rate",
  "Hyperventilation", "Sweating", "Trembling", "Bleeding", "Discharge",
  "Insomnia", "Agitation", "Depression", "Anxiety", "Paranoia", "Hallucination"
]

# diseases database (dictionary)
diagnosis_database = {
  "acute Bronchitis": ['Cough', 'Mucus'],
  "allergy": ['Runny nose', 'Sneezing', 'Itchy Eyes', 'Watery Eyes'],
  "anxiety": ['Increased heart rate', 'Hyperventilation', 'Sweating', 'Trembling'],
  "brain Cancer": ['Headache', 'Blurred vision'],
  "chlamydia": ['Bleeding', 'Discharge'],
  "COVID-19": ['Fever', 'Sore throat', 'Runny nose'],
  "depression": ['Fatigue', 'Imsomnia', 'Agitation'],
  "diarrhea": ['Fever', 'Cramps', 'Bloating', 'Nausea', 'Vomiting'],
  "ear infection": ['Fever', 'Ear Pain'],
  "endometriosis": ['Stomache ache', 'Bleeding'],
  "fibromyalgia": ['Fatigue', 'Depression', 'Anxiety', 'Insomnia', 'Headache'],
  "flu": ['Fever', 'Cough', 'Runny nose'],
  "lupus": ['Fatigue', 'Fever'],
  "lyme disease": ['Fever', 'Fatigue', 'Headache'],
  "mononucleosis": ['Fatigue', 'Fever', 'Sore Throat', 'Headache'],
  "pink eye": ['Runny nose', 'Blurred vision'],
  "pneumonia": ['Cough', 'Fatigue', 'Fever', 'Nausea', 'Vomiting'],
  "schizophrenia": ['Anxiety', 'Paranoia', 'Hallucination'],
}

def get_symptoms():
    return symptoms_database

def get_all_diagnosis():
    return diagnosis_database

def get_diagnosis(user_symptoms):
    # user_symptoms will come in as a string ("0,3,7") from front end, the string will be parsed into a list like [0, 3, 7]
    user_symptoms = [0, 3, 7]

    # initialize match result for all sicknesses
    match_result_array = [0] * 18

    # iterate through each symptom in each disease
    match_disease_index = 0
    max_match_result = 0
    max_match_result_disease = ""
    for key, values in diagnosis_database.items():
        for value in values:
            for i in user_symptoms:
                user_symptom = symptoms_database[i]
                if value == user_symptom:
                    match_result_array[match_disease_index] = match_result_array[match_disease_index] + 1
                    break
        if match_result_array[match_disease_index] > max_match_result:
            max_match_result = match_result_array[match_disease_index]
            max_match_result_disease = key
        match_disease_index = match_disease_index + 1

    print("Based on your current symptoms, your mostly likely sickness is the " +
      max_match_result_disease + ".")

    return max_match_result_disease