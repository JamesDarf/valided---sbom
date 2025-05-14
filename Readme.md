

#  validated SBOM case
cyclonedx validate --input-file sbom_invalid.json 

# Invalidated SBOM case 
 cyclonedx validate --input-file sbom_invalid.json 

 ### 
 ```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.6",
  "version": "one",  // <- 잘못된 타입
  "components": [
    {
      "type": "bucket",       // <- 잘못된 타입명
      "name": "",             // <- 이름 없음
      "version": "N/A",       // <- 권장되지 않는 값
      "purl": "invalid-url"   // <- 잘못된 형식
    }
  ]
}

 ```

 # valided---sbom
