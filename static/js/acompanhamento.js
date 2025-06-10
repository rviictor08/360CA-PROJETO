const statusOptions = ["Em transporte", "Chegando", "Entregue"];
        const linhas = document.querySelectorAll("tbody tr");

        setInterval(() => {
            linhas.forEach(linha => {
                const statusCell = linha.querySelector(".status");
                if (!statusCell) return;
                const atual = statusOptions.indexOf(statusCell.innerText);
                if (atual >= 0) {
                    statusCell.innerText = statusOptions[(atual + 1) % statusOptions.length];
                }
            });
        }, 5000); // troca a cada 5 segundos