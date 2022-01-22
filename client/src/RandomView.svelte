<script>
  let rand = -1;

  function getRand() {
    fetch("./rand")
      .then(d => d.text())
      .then(d => (rand = d));
  }
</script>

<h1>Your number is {rand}!</h1>
<button on:click={getRand}>Get a random number</button>

<a href="#/randomView2">Test link</a>

<style>
    h1 {
        color: red;
    }
</style>
