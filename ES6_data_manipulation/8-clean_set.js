export default function cleanSet(set, string) {
  if (string === '') return '';
  const result = [];
  for (const word of set) {
    if (word.startsWith(string)) {
      result.push(word.slice(string.length));
    }
  }

  return result.join('-');
}
