<script>
    export let cellData = {
            locationName: "Sainsbury's Local",
            locationType: "sains",
            estimatedPrice: 16.06,
            distance: 0.50,
            isOnline: false,
        }
    // if isOnline, we should have a deliveryDate attribute
</script>

<div class="suggestionsCell">
    <div class="upperRow">
        <div class="supermarketDescription">
            <img src={"/supermarketFavicons/" + cellData.locationType + ".png"} class="supermarketFavicon"/>
            <div>
                {cellData.locationName}
            </div>
        </div>
        {#if cellData.isOnline}
            <div>Delivery: {cellData.deliveryDate}</div>
        {:else}
            <div>{cellData.distance} km</div>
        {/if}
    </div>
    <div style="text-align: right;">
        Estimate: £ {cellData.estimatedPrice}
    </div>
</div>

<style>
    .upperRow {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 5px;
    }

    .supermarketFavicon {
        margin-right: 5px;
        border-radius: 5px;
        overflow: hidden;
        width: 20px;
        height: 20px;
    }

    .supermarketDescription {
        display: flex;
        flex-direction: row;
        /*justify-content: space-between;*/
        align-items: center;
    }

    .suggestionsCell {
        margin-top: 5px;
    }
</style>
