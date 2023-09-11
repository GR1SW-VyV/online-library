const coverImages = document.querySelectorAll('.cover-image');

        coverImages.forEach(coverImage => {
            const pdfPath = coverImage.getAttribute('data-path');

            const canvas = document.createElement('canvas');
            const context = canvas.getContext('2d');

            // Cargar el PDF y renderizar la primera página en el canvas
            pdfjsLib.getDocument(pdfPath).promise
            .then(pdfDoc => pdfDoc.getPage(1))
            .then(page => {
                const viewport = page.getViewport({ scale: 1.0 }); // Ajusta la escala según sea necesario
                canvas.width = viewport.width;
                canvas.height = viewport.height;
                const renderContext = {
                    canvasContext: context,
                    viewport: viewport,
                };
                return page.render(renderContext).promise;
            })
            .then(() => {
                // Convertir el canvas en una imagen base64
                const imageDataURL = canvas.toDataURL('image/png');

                // Establecer la imagen base64 como fuente de la imagen en tu HTML
                coverImage.src = imageDataURL;
            })
            .catch(error => {
                console.error('Error al cargar y renderizar el PDF:', error);
            });
        });