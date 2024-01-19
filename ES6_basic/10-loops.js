export default function appendToEachArrayValue(array, appendString) {
  let newArray = [];
  for (const value of array) {
    newArray.append(value);
  }

  return newArray;
}
