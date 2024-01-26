<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Api Call</title>
</head>
<body>
    <select id="table_select">
        <option value="culture">Culture</option>
        <option value="date">Date</option>
        <option value="element_chimique">Elements chimiques</option>
        <option value="engrais">Engrais</option>
        <option value="epandre">Epandre</option>
        <option value="logs">Logs</option>
        <option value="parcelle">Parcelle</option>
        <option value="posseder">Posseder</option>
        <option value="production">Production</option>
        <option value="un">Un</option>
    </select>
    <button onclick=callApi()>Call api</button>
    <div id="result"></div>
</body>
<script>
    async function callApi() {
        const table = document.getElementById("table_select").value
        await fetch(`http://100.117.174.114:8000/${table}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            document.getElementById("result").textContent = JSON.stringify(data)
        })
        .catch(error => console.error(error))
    }
</script>
</html>
