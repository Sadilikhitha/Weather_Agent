const API = "http://127.0.0.1:8000";


// =========================================================
// ELEMENTS
// =========================================================

const cityInput = document.getElementById("cityInput");
const searchForm = document.getElementById("searchForm");
const searchButton = searchForm
    ? searchForm.querySelector("button")
    : null;

const locationButton =
    document.getElementById("locationButton");

const changeCityButton =
    document.getElementById("changeCityButton");

const themeButton =
    document.getElementById("themeButton");


// Left panel
const contextCity =
    document.getElementById("contextCity");

const temperature =
    document.getElementById("temperature");

const feelsLike =
    document.getElementById("feelsLike");

const condition =
    document.getElementById("condition");

const weatherIcon =
    document.getElementById("weatherIcon");

const humidity =
    document.getElementById("humidity");

const wind =
    document.getElementById("wind");

const rainChance =
    document.getElementById("rainChance");

const uv =
    document.getElementById("uv");

const visibility =
    document.getElementById("visibility");

const pressure =
    document.getElementById("pressure");


// Chat
const chatForm =
    document.getElementById("chatForm");

const chatInput =
    document.getElementById("chatInput");

const chatMessages =
    document.getElementById("chatMessages");

const chatButton =
    document.getElementById("chatButton");


// =========================================================
// STATE
// =========================================================

// No default city
let currentWeather = null;

let currentCity = null;


// Keep conversation small to control tokens.
// 12 messages = approximately 6 user/AI turns.
const MAX_HISTORY = 12;

let chatHistory = [];


// =========================================================
// WEATHER ICON
// =========================================================

function getWeatherIcon(condition) {

    const text =
        String(condition || "")
            .toLowerCase();


    if (
        text.includes("thunder") ||
        text.includes("storm")
    ) {
        return "⛈️";
    }


    if (
        text.includes("rain") ||
        text.includes("drizzle") ||
        text.includes("shower")
    ) {
        return "🌧️";
    }


    if (
        text.includes("snow") ||
        text.includes("sleet") ||
        text.includes("blizzard")
    ) {
        return "❄️";
    }


    if (
        text.includes("fog") ||
        text.includes("mist")
    ) {
        return "🌫️";
    }


    if (
        text.includes("cloud") ||
        text.includes("overcast")
    ) {
        return "☁️";
    }


    if (
        text.includes("sun") ||
        text.includes("clear")
    ) {
        return "☀️";
    }


    return "🌤️";
}


// =========================================================
// SET EMPTY LOCATION STATE
// =========================================================

function resetWeatherPanel() {

    currentWeather = null;
    currentCity = null;


    if (contextCity) {
        contextCity.textContent =
            "No location selected";
    }


    if (temperature) {
        temperature.textContent =
            "--°";
    }


    if (feelsLike) {
        feelsLike.textContent =
            "--°";
    }


    if (condition) {
        condition.textContent =
            "Select a location";
    }


    if (weatherIcon) {
        weatherIcon.textContent =
            "🌍";
    }


    if (humidity) {
        humidity.textContent =
            "--%";
    }


    if (wind) {
        wind.textContent =
            "-- km/h";
    }


    if (rainChance) {
        rainChance.textContent =
            "--%";
    }


    if (uv) {
        uv.textContent =
            "--";
    }


    if (visibility) {
        visibility.textContent =
            "-- km";
    }


    if (pressure) {
        pressure.textContent =
            "-- hPa";
    }


    document.body.classList.remove(
        "weather-sunny",
        "weather-cloudy",
        "weather-rain",
        "weather-storm",
        "weather-snow",
        "weather-fog"
    );

}


// =========================================================
// DISPLAY WEATHER
// =========================================================

function displayWeather(data) {

    if (!data) {
        return;
    }


    currentWeather = data;

    currentCity = data.city;


    // -----------------------------------------
    // LEFT PANEL CITY
    // -----------------------------------------

    if (contextCity) {

        contextCity.textContent =
            data.city;

    }


    // -----------------------------------------
    // WEATHER
    // -----------------------------------------

    if (temperature) {

        temperature.textContent =
            `${data.temperature}°`;

    }


    if (feelsLike) {

        feelsLike.textContent =
            `${data.feels_like}°`;

    }


    if (condition) {

        condition.textContent =
            String(data.condition || "")
                .trim();

    }


    if (weatherIcon) {

        weatherIcon.textContent =
            getWeatherIcon(
                data.condition
            );

    }


    // -----------------------------------------
    // METRICS
    // -----------------------------------------

    if (humidity) {

        humidity.textContent =
            `${data.humidity}%`;

    }


    if (wind) {

        wind.textContent =
            `${data.wind_speed} km/h`;

    }


    if (uv) {

        uv.textContent =
            data.uv_index ?? "--";

    }


    if (pressure) {

        pressure.textContent =
            `${data.pressure} hPa`;

    }


    if (visibility) {

        visibility.textContent =
            `${data.visibility} km`;

    }


    // -----------------------------------------
    // RAIN
    // -----------------------------------------

    if (
        rainChance &&
        data.forecast &&
        data.forecast.length > 0
    ) {

        rainChance.textContent =
            `${data.forecast[0].rain_chance}%`;

    }


    // -----------------------------------------
    // WEATHER BACKGROUND
    // -----------------------------------------

    updateWeatherBackground(
        data.condition
    );

}


// =========================================================
// WEATHER BACKGROUND
// =========================================================

function updateWeatherBackground(condition) {

    const weather =
        String(condition || "")
            .toLowerCase();


    document.body.classList.remove(
        "weather-sunny",
        "weather-cloudy",
        "weather-rain",
        "weather-storm",
        "weather-snow",
        "weather-fog"
    );


    if (
        weather.includes("thunder") ||
        weather.includes("storm")
    ) {

        document.body.classList.add(
            "weather-storm"
        );

    }

    else if (
        weather.includes("rain") ||
        weather.includes("drizzle") ||
        weather.includes("shower")
    ) {

        document.body.classList.add(
            "weather-rain"
        );

    }

    else if (
        weather.includes("snow") ||
        weather.includes("sleet")
    ) {

        document.body.classList.add(
            "weather-snow"
        );

    }

    else if (
        weather.includes("fog") ||
        weather.includes("mist")
    ) {

        document.body.classList.add(
            "weather-fog"
        );

    }

    else if (
        weather.includes("cloud") ||
        weather.includes("overcast")
    ) {

        document.body.classList.add(
            "weather-cloudy"
        );

    }

    else {

        document.body.classList.add(
            "weather-sunny"
        );

    }

}


// =========================================================
// LOAD WEATHER
// =========================================================

async function loadWeather(city) {

    city = String(city || "").trim();


    if (!city) {

        showError(
            "Please enter a city name."
        );

        return;

    }


    if (searchButton) {

        searchButton.disabled = true;

        searchButton.textContent =
            "Loading...";

    }


    try {

        const response =
            await fetch(
                `${API}/weather?city=${encodeURIComponent(city)}`
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Unable to get weather."
            );

        }


        if (data.detail) {

            throw new Error(
                data.detail
            );

        }


        displayWeather(data);


        // ------------------------------------------------
        // Reset conversation when changing location.
        // This prevents old city information being reused.
        // ------------------------------------------------

        chatHistory = [];


        if (chatMessages) {

            chatMessages.innerHTML = "";

            addMessage(
                `I'm now using live weather data for ${data.city}. What would you like to know?`,
                "ai"
            );

        }


    } catch (error) {

        console.error(
            "Weather error:",
            error
        );


        showError(
            "Could not find weather for this location."
        );

    } finally {

        if (searchButton) {

            searchButton.disabled =
                false;

            searchButton.textContent =
                "Go";

        }

    }

}


// =========================================================
// SEARCH CITY
// =========================================================

if (searchForm) {

    searchForm.addEventListener(
        "submit",
        function (event) {

            event.preventDefault();


            const city =
                cityInput
                    ? cityInput.value.trim()
                    : "";


            if (!city) {

                showError(
                    "Enter a city first."
                );

                return;

            }


            loadWeather(city);

        }
    );

}


// =========================================================
// CHANGE BUTTON
// =========================================================

if (changeCityButton) {

    changeCityButton.addEventListener(
        "click",
        function () {

            if (cityInput) {

                cityInput.focus();

                cityInput.select();

            }

        }
    );

}


// =========================================================
// MY LOCATION
// =========================================================

if (locationButton) {

    locationButton.addEventListener(
        "click",
        function () {

            if (!navigator.geolocation) {

                showError(
                    "Your browser does not support location detection."
                );

                return;

            }


            locationButton.disabled =
                true;

            locationButton.innerHTML =
                "⌖ Detecting...";


            navigator.geolocation.getCurrentPosition(

                async function (position) {

                    try {

                        const latitude =
                            position.coords.latitude;

                        const longitude =
                            position.coords.longitude;


                        // Free reverse geocoding API
                        const response =
                            await fetch(
                                `https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${latitude}&longitude=${longitude}&localityLanguage=en`
                            );


                        if (!response.ok) {

                            throw new Error(
                                "Reverse geocoding failed."
                            );

                        }


                        const locationData =
                            await response.json();


                        const city =
                            locationData.city ||
                            locationData.locality ||
                            locationData.principalSubdivision;


                        if (!city) {

                            throw new Error(
                                "Could not determine city."
                            );

                        }


                        if (cityInput) {

                            cityInput.value =
                                city;

                        }


                        await loadWeather(
                            city
                        );


                    } catch (error) {

                        console.error(
                            "Location error:",
                            error
                        );


                        showError(
                            "Unable to determine your location. Try searching your city manually."
                        );

                    } finally {

                        locationButton.disabled =
                            false;

                        locationButton.innerHTML =
                            "⌖ <span>My location</span>";

                    }

                },


                function (error) {

                    console.error(
                        "Geolocation error:",
                        error
                    );


                    let message =
                        "Unable to detect your location.";


                    if (
                        error.code ===
                        error.PERMISSION_DENIED
                    ) {

                        message =
                            "Location permission was denied. Please allow location access in your browser.";

                    }


                    showError(
                        message
                    );


                    locationButton.disabled =
                        false;

                    locationButton.innerHTML =
                        "⌖ <span>My location</span>";

                },


                {
                    enableHighAccuracy: true,
                    timeout: 15000,
                    maximumAge: 300000
                }

            );

        }
    );

}


// =========================================================
// CHAT MESSAGE
// =========================================================

function addMessage(text, type) {

    if (!chatMessages) {
        return;
    }


    const row =
        document.createElement("div");


    row.className =
        type === "user"
            ? "message-row user-row"
            : "message-row ai-row";


    const message =
        document.createElement("div");


    message.className =
        `message ${type}-message`;


    if (type === "ai") {

        const label =
            document.createElement("div");


        label.className =
            "message-label";


        label.textContent =
            "SkyCast";


        message.appendChild(
            label
        );

    }


    const textElement =
        document.createElement("p");


    textElement.textContent =
        String(text || "");


    message.appendChild(
        textElement
    );


    row.appendChild(
        message
    );


    chatMessages.appendChild(
        row
    );


    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}


// =========================================================
// KEEP ONLY LIMITED CHAT HISTORY
// =========================================================

function addToHistory(
    role,
    content
) {

    chatHistory.push({
        role: role,
        content: content
    });


    // Keep only latest 12 messages
    if (
        chatHistory.length >
        MAX_HISTORY
    ) {

        chatHistory =
            chatHistory.slice(
                -MAX_HISTORY
            );

    }

}


// =========================================================
// ASK AI
// =========================================================

async function askAI(question) {

    question =
        String(question || "")
            .trim();


    if (!question) {
        return;
    }


    // -----------------------------------------
    // Add user message
    // -----------------------------------------

    addMessage(
        question,
        "user"
    );


    addToHistory(
        "user",
        question
    );


    if (chatInput) {

        chatInput.value =
            "";

    }


    if (chatButton) {

        chatButton.disabled =
            true;

        chatButton.textContent =
            "⏳";

    }


    // -----------------------------------------
    // Thinking message
    // -----------------------------------------

    const thinking =
        document.createElement("div");


    thinking.className =
        "message-row ai-row";


    thinking.innerHTML = `
        <div class="message ai-message">
            <div class="message-label">SkyCast</div>
            <p>Thinking...</p>
        </div>
    `;


    if (chatMessages) {

        chatMessages.appendChild(
            thinking
        );

        chatMessages.scrollTop =
            chatMessages.scrollHeight;

    }


    try {

        // -----------------------------------------
        // Send current weather + history
        // -----------------------------------------

        const response =
            await fetch(
                `${API}/ask`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        question:
                            question,

                        weather_data:
                            currentWeather,

                        chat_history:
                            chatHistory

                    })

                }
            );


        const data =
            await response.json();


        thinking.remove();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "AI request failed."
            );

        }


        if (!data.answer) {

            throw new Error(
                "Empty AI response."
            );

        }


        // -----------------------------------------
        // Add AI response to history
        // -----------------------------------------

        addToHistory(
            "assistant",
            data.answer
        );


        addMessage(
            data.answer,
            "ai"
        );


    } catch (error) {

        console.error(
            "AI error:",
            error
        );


        thinking.remove();


        // Remove failed user message
        chatHistory =
            chatHistory.filter(
                (message, index) =>
                    index !==
                    chatHistory.length - 1
            );


        addMessage(
            "Sorry, I couldn't process that request. Please try again.",
            "ai"
        );

    } finally {

        if (chatButton) {

            chatButton.disabled =
                false;

            chatButton.textContent =
                "↑";

        }

    }

}


// =========================================================
// CHAT SUBMIT
// =========================================================

if (chatForm) {

    chatForm.addEventListener(
        "submit",
        function (event) {

            event.preventDefault();


            const question =
                chatInput
                    ? chatInput.value.trim()
                    : "";


            if (!question) {
                return;
            }


            askAI(question);

        }
    );

}


// =========================================================
// ENTER TO SEND
// =========================================================

if (chatInput) {

    chatInput.addEventListener(
        "keydown",
        function (event) {

            if (
                event.key === "Enter" &&
                !event.shiftKey
            ) {

                event.preventDefault();


                chatForm.requestSubmit();

            }

        }
    );

}


// =========================================================
// QUICK CHAT BUTTONS
// =========================================================

document
    .querySelectorAll(
        "[data-question]"
    )
    .forEach(
        button => {

            button.addEventListener(
                "click",
                function () {

                    const question =
                        button.dataset.question;


                    askAI(
                        question
                    );

                }
            );

        }
    );


// =========================================================
// THEME
// =========================================================

if (themeButton) {

    themeButton.addEventListener(
        "click",
        function () {

            document.body.classList.toggle(
                "light"
            );


            if (
                document.body.classList.contains(
                    "light"
                )
            ) {

                themeButton.textContent =
                    "☀️";

            } else {

                themeButton.textContent =
                    "☾";

            }

        }
    );

}


// =========================================================
// ERROR
// =========================================================

function showError(message) {

    console.error(
        message
    );


    // If your HTML has an error box,
    // use it.
    const errorBox =
        document.getElementById(
            "error"
        );


    const errorMessage =
        document.getElementById(
            "errorMessage"
        );


    if (
        errorBox &&
        errorMessage
    ) {

        errorMessage.textContent =
            message;

        errorBox.classList.remove(
            "hidden"
        );


        setTimeout(
            function () {

                errorBox.classList.add(
                    "hidden"
                );

            },
            5000
        );

    } else {

        // fallback
        alert(message);

    }

}


// =========================================================
// INITIAL STATE
// =========================================================

// IMPORTANT:
// There is NO default city here.
//
// The app waits for:
// 1. My Location
// OR
// 2. User searching for a city.
//
// =========================================================

resetWeatherPanel();
