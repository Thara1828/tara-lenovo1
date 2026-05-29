// Helpline numbers
const helpline = {
    India: { police: "112", ambulance: "108", child: "1098" },
    USA: { police: "911", ambulance: "911", child: "1-800-422-4453" },
    UK: { police: "999", ambulance: "999", child: "0800 1111" },
    Germany: { police: "110", ambulance: "112", child: "116111" },
    UAE: { police: "999", ambulance: "998", child: "800111" }
};

// Country-specific bank map links
const bankMapLinks = {
    India: "https://www.google.com/maps/search/bank+in+India",
    USA: "https://www.google.com/maps/search/bank+in+USA",
    UK: "https://www.google.com/maps/search/bank+in+UK",
    Germany: "https://www.google.com/maps/search/bank+in+Germany",
    UAE: "https://www.google.com/maps/search/bank+in+UAE"
};

// Language translations
const translations = {
    English: {
        greeting: "Hello! Your travel assistant is here.",
        country: "Country",
        police: "Police",
        ambulance: "Ambulance",
        child: "Child Helpline",
        services: "Services",
        currency: "Currency Exchange",
        travel: "Travel Help"
    },
    Tamil: {
        greeting: "வணக்கம்! உங்கள் பயண உதவியாளர் இங்கே.",
        country: "நாடு",
        police: "போலீஸ்",
        ambulance: "அம்புலன்ஸ்",
        child: "குழந்தைகள் உதவி",
        services: "சேவைகள்",
        currency: "நாணய மாற்றம்",
        travel: "பயண உதவி"
    },
    Hindi: {
        greeting: "नमस्ते! आपका यात्रा सहायक यहाँ है।",
        country: "देश",
        police: "पुलिस",
        ambulance: "एम्बुलेंस",
        child: "चाइल्ड हेल्पलाइन",
        services: "सेवाएँ",
        currency: "मुद्रा विनिमय",
        travel: "यात्रा सहायता"
    },
    Spanish: {
        greeting: "¡Hola! Su asistente de viaje está aquí.",
        country: "País",
        police: "Policía",
        ambulance: "Ambulancia",
        child: "Línea de ayuda infantil",
        services: "Servicios",
        currency: "Cambio de moneda",
        travel: "Ayuda de viaje"
    },
    French: {
        greeting: "Bonjour! Votre assistant de voyage est ici.",
        country: "Pays",
        police: "Police",
        ambulance: "Ambulance",
        child: "Ligne d'aide pour enfants",
        services: "Services",
        currency: "Échange de devises",
        travel: "Aide au voyage"
    }
};

function goSupport() {
    const country = document.getElementById("country").value;
    const language = document.getElementById("language").value;
    localStorage.setItem("country", country);
    localStorage.setItem("language", language);
    window.location.href = "/support";
}

window.onload = function () {
    const country = localStorage.getItem("country");
    const language = localStorage.getItem("language") || "English";

    if (country && document.getElementById("details")) {
        const d = helpline[country];
        const t = translations[language];

        document.getElementById("details").innerHTML = `
            <p>${t.greeting}</p>
            <p><b>${t.country}:</b> ${country}</p>
            <p>🚓 ${t.police}: ${d.police}</p>
            <p>🚑 ${t.ambulance}: ${d.ambulance}</p>
            <p>🧒 ${t.child}: ${d.child}</p>
            <h3>${t.services}</h3>
            <button onclick="openBank()">${t.currency}</button>
            <button onclick="travelHelp()">${t.travel}</button>
        `;
    }
};

function openBank() {
    const country = localStorage.getItem("country");
    const link = bankMapLinks[country] || "https://www.google.com/maps/search/bank+near+me";
    window.open(link, "_blank");
}

function travelHelp() {
    const language = localStorage.getItem("language") || "English";
    const t = translations[language];

    if (language === "Tamil") alert("பயண தொடர்புடைய கேள்விகள் AI உதவியால் பதில் அளிக்கப்படும்.");
    else if (language === "Hindi") alert("यात्रा से संबंधित प्रश्न AI सहायक द्वारा हल किए जाएंगे।");
    else if (language === "Spanish") alert("Las consultas de viaje serán atendidas por el asistente AI.");
    else if (language === "French") alert("Les questions liées au voyage seront traitées par l'assistant AI.");
    else alert("Travel-related queries will be handled by AI Agent.");
}
