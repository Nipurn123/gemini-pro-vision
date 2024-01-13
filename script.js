const form = document.getElementById('image-form');
const result = document.getElementById('result');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const formData = new FormData(form);

    fetch('/generate_text_from_image', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            result.textContent = data.error;
        } else {
            result.textContent = data.result;
        }
    })
    .catch(error => {
        result.textContent = `Error generating text from image: ${error}`;
    });
});
