<script>
    export let backgroundColor = "#fffefe";
    export let isFloating = false
</script>

<div class="card{isFloating ? ' floatingCard' : ''}" style="background-color: {backgroundColor}">
    <slot>
    </slot>
</div>

<style>
    .card{
        border-radius: 20px;

        border-color: rgba(0, 0, 0, 0);
        border-style: solid;
        border-width: 1px;

        transition:  .3s;
    }

    .floatingCard{
        box-shadow: 0 22px 70px 4px rgba(0, 0, 0, 0.06);
    }
</style>
