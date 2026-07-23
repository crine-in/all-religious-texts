const fs = require('fs');
const path = require('path');

function searchByKeyword(filePath, keyword) {
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  return data.filter(verse => verse.text && verse.text.toLowerCase().includes(keyword.toLowerCase()));
}

const samplePath = path.join(__dirname, '..', 'isha.json');
if (fs.existsSync(samplePath)) {
  const matches = searchByKeyword(samplePath, 'vāsyam');
  console.log(`Found ${matches.length} matching verses:`);
  console.log(matches);
}
