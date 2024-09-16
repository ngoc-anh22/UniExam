document.querySelectorAll('input[name="exemption"]').forEach((elem) => {
    elem.addEventListener("change", function(event) {
        const foreignLanguageSection = document.getElementById("foreign_language_section");
        if (event.target.value === "yes") {
            foreignLanguageSection.style.display = "none";
        } else {
            foreignLanguageSection.style.display = "flex";
        }
    });
});