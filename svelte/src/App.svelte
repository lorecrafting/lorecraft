<script>
	export let name;
	export let desc;
	export let contents = [];
	export let exits = [];

	function handleWindowLoad() {
		window.Evennia.emitter.on("room_data", function(empty, roomData) {
			name = roomData.name;
			desc = roomData.desc;
			contents = roomData.contents;
			exits = roomData.exits;
		})
	}

	function handleClickExit(exit) {
		Evennia.msg("text", [exit])
	}
</script>

<svelte:window on:load={handleWindowLoad}/>

<main>
	<h1>{name}</h1>
	<p>{@html desc}</p>
	<p>{contents}</p>
	<p> {#if exits.length > 0}
			You can go:
			<br>
		{/if}
		{#each exits as exit}
		<a on:click={() => handleClickExit(exit)}>{exit}</a>
		<br>
		{/each}
	</p>
</main>

<style>
	main {
		text-align: center;
		padding: 2em;
		max-width: 240px;
		margin: 0 auto;
	}

	p {
		text-align: left;
	}

	p::first-letter {
 	   text-transform:capitalize;
	}

	h1 {
		text-transform: uppercase;
		font-size: 3em;
		font-weight: 100;
		margin-bottom: 1.5rem;
	}

	a {
		text-decoration: underline;
	}
	a:hover {
		cursor: pointer;
		color: rgb(255, 183, 183);
		text-decoration: underline;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
