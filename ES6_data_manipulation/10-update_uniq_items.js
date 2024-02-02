export default function updateUniqueItem(set) {
  try {
    return set.forEach((value, key, map) => {
      if (value === 1) {
        map.set(key, 100);
      }
    });
  } catch (err) {
    throw new Error('Cannot process');
  }
}
