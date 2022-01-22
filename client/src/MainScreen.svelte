<script>
    import Card from "./Card.svelte";
    import { push } from 'svelte-spa-router'

    let currentShop = {
        itemNames: ["Water", "Chicken"], // Names of things in the shopping list
        estimatedCost: 16.06, // Total cost in pounds
        suggestedLocation: "Sainsbury's Local", // Location Name
        suggestedLocationType: "sains", // We can use this to maybe show a favicon later next to the location name
    }

    let pastShops = [
        {
            locationName: "Sainsbury's Local",
            cost: 12.05,
            locationType: "sains"
        },
        {
            locationName: "Tesco Express",
            cost: 13.20,
            locationType: "tesco"
        },
        {
            locationName: "Waitrose",
            cost: 15.20,
            locationType: "waitrose"
        },
    ]
</script>

<div id="content">
    <!-- Title element -->
    <h1>
        My Shopping
    </h1>

    <!-- Next Shop -->
    <div class="listElement" on:click={() => push('/nextShop')}>
        <Card isFloating="true">
            <div class="cardContent">
                <h2>
                    My Next Shop
                </h2>
                <div class="estimateCardContent">
                    <div>
                        {currentShop.suggestedLocation}
                    </div>
                    <div id="costEstimate">
                        Estimate:
                        <br/>
                        £{currentShop.estimatedCost}
                    </div>
                </div>
            </div>
        </Card>
    </div>

    <br/>

    {#each pastShops as pastShop}
        <div class="listElement pastShop">
            <Card backgroundColor="white">
                <div class="cardContent">
                    <div class="estimateCardContent">
                    <div>
                        {pastShop.locationName}
                    </div>
                    <div id="costEstimate">
                        Cost:
                        <br/>
                        £{pastShop.cost}
                    </div>
                </div>
                </div>
            </Card>
        </div>
    {/each}
</div>

<style>
    h1 {
        margin-left: 8px;
    }

    #content {
        padding: 10px;
    }

    .estimateCardContent {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }

    #costEstimate{
        text-align: right;
    }

    .cardContent {
        margin: 20px;
    }

    .listElement{
        margin-top: 10px;
        cursor: pointer;
    }

    .pastShop{
        transform: scale(0.95);
    }
</style>
