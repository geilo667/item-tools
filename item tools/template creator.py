import json

def create_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def replace_characters_in_json(json_data, replacement_string, target_string):
    for key, value in json_data.items():
        if isinstance(value, str):
            json_data[key] = value.replace(target_string, replacement_string)
        elif isinstance(value, dict):
            json_data[key] = replace_characters_in_json(value, replacement_string, target_string)
    return json_data

def main():
    # Definieren Sie Ihre JSON-Daten
    json_data = {
  "type": "minecraft:crafting_shaped",
  "pattern": [
    "###",
    " / ",
    " / "
  ],
  "key": {
    "#": {
      "item": "minecraft:<target_string>"
    },
    "/": {
      "item": "minecraft:stick"
    }
  },
  "result": {
    "id": "minecraft:diamond_pickaxe",
    "components": {
      "minecraft:custom_model_data": 1,
      "minecraft:custom_name": "[{'text':'<target_string> Pickaxe','italic':false}]"
    }
}

    }

    # Benutzereingabe für den Ersatz-String und den Ziel-String
    replacement_string = input("Geben Sie den Ersatz-String ein: ")
    target_string = "<target_string>"

    # Ersetzen Sie die Zeichen in der JSON-Datenstruktur
    json_data_replaced = replace_characters_in_json(json_data, replacement_string, target_string)

    # Erstellen Sie die JSON-Datei
    output_filename = f"{replacement_string}_pickaxe.json"
    create_json_file(json_data_replaced, output_filename)
    print(f"JSON-Datei '{output_filename}' erfolgreich erstellt.")

if __name__ == "__main__":
    main()
