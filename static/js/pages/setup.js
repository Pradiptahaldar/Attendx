document.addEventListener("DOMContentLoaded", () => {

    const step1 = document.getElementById("step1");
    const step2 = document.getElementById("step2");

    const continueBtn = document.getElementById("continueBtn");
    const backBtn = document.getElementById("backToStep1");

    const organizationName =
        document.getElementById("organizationName");

    const organizationType =
        document.getElementById("organizationType");


    // STEP 1 → STEP 2

    continueBtn.addEventListener("click", () => {

        if (!organizationName.value.trim()) {
            organizationName.focus();
            return;
        }

        if (!organizationType.value) {
            organizationType.focus();
            return;
        }

        step1.style.display = "none";
        step2.style.display = "block";

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    });


    // STEP 2 → STEP 1

    backBtn.addEventListener("click", () => {

        step2.style.display = "none";
        step1.style.display = "block";

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    });

});