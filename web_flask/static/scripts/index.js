// Sample data for pharmacy shops (replace with actual data)
const pharmacyShops = [
    {
        name: "Pharmacy A",
        address: "123 Main St",
        drug: "Drug X",
        price: "$10.99"
    },
    {
        name: "Pharmacy B",
        address: "456 Elm St",
        drug: "Drug Y",
        price: "$5.99"
    },
    // Add more data entries as needed
];

// Function to generate cards based on search results
function generateCards(results) {
    const carousel = document.querySelector(".carousel");

    // Clear previous cards
    carousel.innerHTML = "";

    // Generate new cards based on search results
    results.forEach(result => {
        const card = document.createElement("div");
        card.classList.add("card");

        // Create card content
        card.innerHTML = `
            <div class="card-header">
                <h3>${result.name}</h3>
                <p>${result.address}</p>
            </div>
            <div class="card-body">
                <p>Drug: ${result.drug}</p>
                <p>Price: ${result.price}</p>
            </div>
        `;

        carousel.appendChild(card);
    });
}

// Function to handle the search
function handleSearch() {
    const searchTerm = document.getElementById("searchInput").value.toLowerCase();
    const searchResults = pharmacyShops.filter(shop => shop.drug.toLowerCase() === searchTerm);

    generateCards(searchResults);
}

// Attach the search function to the search button click event
document.getElementById("searchButton").addEventListener("click", handleSearch);

