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
        <div>{cellData.locationName}</div>
        {#if cellData.isOnline}
            <div>{cellData.deliveryDate}</div>
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

    .suggestionsCell {
        margin-top: 5px;
    }
</style>
