document.addEventListener("DOMContentLoaded", function () {
    const pdfViewer = document.getElementById("pdfViewer");
    const currentPageSpan = document.getElementById("currentPage");
    const totalPagesSpan = document.getElementById("totalPages");
    const btnPreviousPage = document.getElementById("btnPrevious");
    const btnNextPage = document.getElementById("btnNext")
    let currentPage = pageCounter; // Inicialmente en la página 1
    let totalPages = 1;

    pdfjsLib
        .getDocument(pdfUrl)
        .promise.then(function (pdfDoc) {
        // Carga la primera página del PDF
        totalPages = pdfDoc.numPages;
        totalPagesSpan.textContent = totalPages;
        return pdfDoc.getPage(1);
    })
        .then(function (page) {

            const scale = 1.0;
            const viewport = page.getViewport({scale: scale});

            // Crea un elemento canvas para mostrar la página
            const canvas = document.createElement("canvas");
            const context = canvas.getContext("2d");
            canvas.height = viewport.height;
            canvas.width = viewport.width;

            // Agrega el canvas al visor de PDF
            pdfViewer.innerHTML = ""; // Limpia el contenedor si hay contenido previo
            pdfViewer.appendChild(canvas);

            // Muestra la página en el canvas
            page.render({
                canvasContext: context,
                viewport: viewport,
            });

            //Deshabilita botones segun el numero de pagina
            if (currentPage === 1) {
                btnPreviousPage.classList.add('d-none')
            }
            if (currentPage === totalPages) {
                btnNextPage.classList.add('d-none')
            }

            updatePage()

        });


    // Actualiza el número de página y muestra la página correspondiente
    function updatePage() {
        if (pdfViewer.firstChild) {
            pdfViewer.firstChild.remove(); // Elimina el canvas actual
        }

        pdfjsLib
            .getDocument(pdfUrl)
            .promise.then(function (pdfDoc) {
            if (currentPage < 1) {
                currentPage = 1;
            } else if (currentPage > pdfDoc.numPages) {
                currentPage = pdfDoc.numPages;
            }

            currentPageSpan.textContent = currentPage;

            totalPages = pdfDoc.numPages;
            totalPagesSpan.textContent = totalPages;

            return pdfDoc.getPage(currentPage);
        })
            .then(function (page) {
                const scale = 1.0;
                const viewport = page.getViewport({scale: scale});

                const canvas = document.createElement("canvas");
                const context = canvas.getContext("2d");
                canvas.height = viewport.height;
                canvas.width = viewport.width;

                pdfViewer.appendChild(canvas);

                page.render({
                    canvasContext: context,
                    viewport: viewport,
                });
            });
    }
});