# validate_sbom.py
import json
import jsonschema

# 파일 열기
# with open('sbom.json') as sbom_file: # Pass case
with open('sbom_invalid_2.json') as sbom_file: # Fail case
    sbom = json.load(sbom_file)


with open('bom-1.6.schema.json') as schema_file:
    schema = json.load(schema_file)

# 유효성 검사 수행
try:
    jsonschema.validate(instance=sbom, schema=schema)
    print("✅ Passed: Document is a valid CycloneDX v1.6 SBOM")
except jsonschema.exceptions.ValidationError as e:
    print("❌ Nope: Invalid SBOM!")
    print("error:", e.message)

