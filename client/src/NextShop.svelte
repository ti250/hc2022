<script>
    import SuggestionsCell from "./SuggestionsCell.svelte";
    import { slide } from 'svelte/transition';

    let isExpanded = false;

    function toggle(){
        isExpanded = !isExpanded;
    }

    let suggestions = [
        {
            locationName: "Sainsbury's Local",
            locationType: "sains",
            estimatedPrice: 16.06,
            distance: 0.50,
            isOnline: false,
        },
        {
            locationName: "Ocado",
            locationType: "ocado",
            estimatedPrice: 18.90,
            deliveryDate: "23/Jan/2022",
            isOnline: true,
        },
        {
            locationName: "Tesco",
            locationType: "tesco",
            estimatedPrice: 17.06,
            distance: 1.0,
            isOnline: false,
        },
    ]

    $: topSuggestion = suggestions[0];

    let items = [
        {name: "apple", quantity: 2}
    ]

    function changeForKey(key, change)
    {
        // TODO (ti250): if the quantity for the key goes to 0, then delete
        function changeForKeyInternal()
        {
            items[key] += change;
            if (items[key] <= 0)
            {
                delete items[key]
            }
            items = items;
        }
        return changeForKeyInternal;
    }
</script>

<h1>
    My Next Shop
</h1>

<!-- Default suggestion -->
<div class="suggestion">
    <SuggestionsCell cellData={topSuggestion}/>
</div>

{#if isExpanded}
    <div transition:slide>
        {#each suggestions.slice(1) as suggestion}
            <div class="suggestion">
                <SuggestionsCell cellData={suggestion}/>
            </div>
        {/each}
    </div>
{/if}

<button on:click={toggle} id="expandButton" class="decorated"> <span> {isExpanded ? "▲ Show Less" : "▼ Show More"} </span> </button>

{#each items as item}
    <div class="itemCell">
        <div>
            ・{item.name}
        </div>
        <div>
            {item.quantity}
        </div>
    </div>
{/each}

<style>
    #content {
        padding: 10px;
    }

    #expandButton {
        width: 100%;
        border: none;
        background: none;
    }

    .suggestion {
        margin-bottom: 10px;
    }

    /* headlines with lines from https://stackoverflow.com/questions/15557627/heading-with-horizontal-line-on-either-side */
    .decorated{
         overflow: hidden;
         text-align: center;
     }
    .decorated > span{
        position: relative;
        display: inline-block;
    }
    .decorated > span:before, .decorated > span:after{
        content: '';
        position: absolute;
        top: 50%;
        border-bottom: 1px solid;
        width: 100vw;
        margin: 0 15px;
    }
    .decorated > span:before{
        right: 95%;
    }
    .decorated > span:after{
        left: 95%;
    }
</style>
