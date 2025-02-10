
document.addEventListener('mouseup', function(event){
    const selectedText = window.getSelection().toString().trim();
    if (selectedText!== '' && selectedText.length >50){
        console.log("Selected Text:", selectedText);
        fetch('http://localhost:5000/summary', {
            method : 'POST',
            headers : {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({ text: selectedText})
        })
        .then(response => response.json())
        .then(data => {
            alert(`summary : ${data.summary}`);
        })
        .catch(error => {
            console.error('Error :', error );
        });
    }

});