document.addEventListener("DOMContentLoaded", function () {
    const pdfViewer = document.getElementById("pdfViewer");
    const currentPageSpan = document.getElementById("currentPage");
    const totalPagesSpan = document.getElementById("totalPages");
    let currentPage = 1; // Inicialmente en la página 1
    let totalPages = 1;
    let pdfUrl; // Declara pdfUrl como variable global


    pdfUrl = "../../static/harry-potter.pdf"; // Ruta al archivo PDF en la carpeta "pdfs"

    // Crea un nuevo visor de PDF
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

            // OJO: Actualiza el número de página actual del documento PDF
            currentPage = 1;
            updatePage()

           // currentPageSpan.textContent = currentPage;
        });


    // Función para cambiar a la página siguiente
    function nextPage() {
        currentPage += 1;
        updatePage();
    }

    // Función para cambiar a la página anterior
    function prevPage() {
        currentPage -= 1;
        updatePage();
    }

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

    // Escucha eventos de los botones para cambiar de página
    const nextPageButton = document.getElementById("nextPage");
    nextPageButton.addEventListener("click", nextPage);

    const prevPageButton = document.getElementById("prevPage");
    prevPageButton.addEventListener("click", prevPage);
});
  