

function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];
}
const form = document.getElementById('form1');

function renderiza_grafico(event){
    event.preventDefault();
    const url = 'http://localhost:8000/dados_graficos';
    const head = this.head.value;
    const type = this.type.value;
    console.log(head)
    fetch(url,{
        method: 'get',
        headers:{'head':head,'type':type}
    }).then(function(result){
        return result.json();
    }).then(function(data){
        const ctx = document.getElementById("graficos").getContext('2d');
        var  cores = gera_cor(qtd = 20);
        const myChart = new Chart(ctx,{
            type: 'line',
            data: {
                labels: data["time"],
                datasets: [{
                    label: data["sum"],
                    data: data["position"],
                    backgroundColor: cores[0],
                    borderColor: cores[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
           
        })
    })
}

form.addEventListener('submit',renderiza_grafico);