<script>
	export let name;
	export let desc;
	export let contents;
	export let exits;

	function handleWindowLoad() {
		window.Evennia.emitter.on("room_data", function(empty, roomData) {
		name = roomData.name;
		desc = roomData.desc;
		contents = roomData.contents;
		exits = roomData.exits;
		console.log(roomData)})
	}
</script>

<svelte:window on:load={handleWindowLoad}/>

<main>
	<h1>{name}</h1>
	<p>{desc}</p>
	<p>{contents}</p>
	<p>{exits}</p>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
