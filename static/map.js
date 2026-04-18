const map = L.map("map").setView([40.2, -82.9], 7);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
}).addTo(map);

fetch("/api/trails")
    .then(res => res.json())
    .then(data => {
        L.geoJSON(data, {
            style: { color: "green", weight: 3 },
            onEachFeature: (feature, layer) => {
                layer.on("click", () => {
                    window.location.href = `/trail/${feature.properties.id}`;
                });
            }
        }).addTo(map);
    });
