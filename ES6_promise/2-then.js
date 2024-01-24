export default function handleResponseFromAPI(promise) {
  promise
    .then(() => {
      return { status: 200, body: 'success' };
    })
    .catch(() => {
      return new Error('');
    })
    .then(() => {
      console.log('Got a response from the API');
    });
}
