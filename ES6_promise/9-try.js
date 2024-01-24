export default function guardrail(mathFunction) {
  const array = [];

  try {
    array.push(mathFunction());
  } catch (err) {
    array.push(err.message);
  }
  array.push('Guardrail was processed');
  return array;
}
