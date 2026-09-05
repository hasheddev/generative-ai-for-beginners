from openai import OpenAI
import json
import pandas as pd

df = pd.read_csv("data/transcriptions.csv")

client = OpenAI()

function = {
    "type": "function",
    "function": {
        "name": "save_patient_info",
        "description": "saves patient medical info",
        "parameters": {
            "type": "object",
            "properties": {
                "recommended_treatment": {
                    "type": "string",
                    "description": "The recommended treatment or procedure extracted from the text.",
                },
                "icd_code": {
                    "type": "string",
                    "description": "The corresponding ICD-10 code for the condition or recommended treatment.",
                },
                "medical_specialty": {
                    "type": "string",
                    "description": "The medical specialty relevant to the patient transcription",
                },
                "age": {
                    "type": "integer",
                    "description": "Patient age extracted from transcription, or null if not mentioned.",
                },
            },
            "required": [
                "age",
                "icd_code",
                "recommended_treatment",
                "medical_specialty",
            ],
        },
        "result": {
            "type": "string",
        },
    },
}

system = {
    "role": "system",
    "content": (
        "You are a medical data extraction specialist. From the given transcript extract the patient's age, "
        "medical specialty, recommended treatment, and map the treatment/condition "
        "to its matching ICD code."
    ),
}

new_data = []

for transcript in df["transcription"]:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            system,
            {"role": "user", "content": transcript},
        ],
        tools=[function],
        tool_choice={
            "type": "function",
            "function": {"name": "save_patient_info"},
        },
    )

    tool_calls = response.choices[0].message.tool_calls
    if tool_calls:
        arguments_json = tool_calls[0].function.arguments
        data = json.loads(arguments_json)
        new_data.append(data)

df_structured = pd.DataFrame(new_data)
print(df_structured)
## if response.choices[0].finish_reason=='tool_calls':