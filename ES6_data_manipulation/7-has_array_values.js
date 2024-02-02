export default function hasValuesFromArray(set, array) {
  const initalLength = set.size;
  for (const ele of array) {
    set.add(ele);
  }
  return set.size === initalLength;
}
