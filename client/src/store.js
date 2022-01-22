import { writable } from "svelte/store";

let defaultSuggestions = [
        {
            locationName: "Sainsbury's Local",
            locationType: "sains",
            estimatedPrice: 0.00,
            distance: 500,
            isOnline: false,
        },
        {
            locationName: "Sainsbury's Local",
            locationType: "sains",
            estimatedPrice: 0.00,
            distance: 500,
            isOnline: false,
        },
]

// let defaultSuggestions = [{
//             locationName: "Sainsbury's Local",
//             locationType: "sains",
//             estimatedPrice: 16.06,
//             distance: 0.50,
//             isOnline: false,
//         },
//         {
//             locationName: "Ocado",
//             locationType: "ocado",
//             estimatedPrice: 18.90,
//             deliveryDate: "23/Jan/2022",
//             isOnline: true,
//         },
//         {
//             locationName: "Tesco",
//             locationType: "tesco",
//             estimatedPrice: 17.06,
//             distance: 1.0,
//             isOnline: false,
//         },]

export const suggestions = writable(JSON.parse(localStorage.getItem("suggestions")) || defaultSuggestions);
export const items = writable(JSON.parse(localStorage.getItem("items")) || [{name: "Apples", quantity: 2}
]);
