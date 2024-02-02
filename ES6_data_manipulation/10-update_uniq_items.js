export default function updateUniqueItem(set) {
  return set.forEach((value, key, map) => {
    if (value === 1) {
      map.set(key, 100);
    }
  });
}
