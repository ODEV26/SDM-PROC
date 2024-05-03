fetch('http://127.0.0.1:8000/proyecto-c/login/success')
.then(response => response.json())
.then(data => {
    const container = document.getElementById('plate-list');
    data.forEach(plate => {
        const plateItem = document.createElement("div");
        plateItem.classList.add("plate-item");
        const plateNumber = document.createElement("h3");
        plateNumber.textContent = `Placa: ${plate.matricula}`;
        const plateImage = document.createElement("img");
        plateImage.src = "{{ url_for('static', path='" + plate.ruta_imagen + "') }}";
        const entryDate = document.createElement("p");
        entryDate.textContent = `fecha de entrada: ${plate.fecha_hora_entrada}`;
        const outDate = document.createElement("p");
        outDate.textContent = `fecha de salida: ${plate.fecha_hora_salida}`;
        const inParking = document.createElement("p");

        inParking.textContent = `Dentro de estacionamiento: ${plate.dentro_de_estacionamiento}`;
        plateItem.appendChild(plateImage);
        plateItem.appendChild(plateNumber);
        plateItem.appendChild(entryDate);
        plateItem.appendChild(outDate);
        plateItem.appendChild(inParking);
        container.appendChild(plateItem);
    });
})

.catch(error => {
    console.error('Error:', error);
});