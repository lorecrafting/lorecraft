<script>
	export let name;
	export let desc;
	export let contents = [];
	export let characters = [];
	export let exits = [];

	function handleWindowLoad() {
		Evennia.init()
		window.Evennia.emitter.on("room_data", function(empty, roomData) {
			name = roomData.name;
			desc = roomData.desc;
			contents = _formatContents(roomData.contents);
			characters = _formatCharacters(roomData.characters);
			exits = roomData.exits;
		})
	}

	function handleClickExit(exit) {
		Evennia.msg("text", [exit])
	}


	function _formatContents(contents) {
		let roomItems = contents.map( item => `a ${item}`)

		if (roomItems.length === 1) {
			return `You see ${roomItems[0]}.`
		}
		if (roomItems.length > 1) {
			let lastItem = roomItems.pop();
			return `You see ${roomItems.join(", ")}, and ${lastItem}.`
		}
		return null
	}

	function _formatCharacters(characters) {
		if (characters.length === 1) {
			return `${characters[0]} is here.`
		}
		if (characters.length === 2) {
			return `${characters[0]} and ${characters[1]} are here.`
		}
		if (characters.length > 2) {
			let lastChar = characters.pop();
			return `${characters.join(", ")}, and ${lastChar} are here.`
		}
	}
</script>

<svelte:window on:load={handleWindowLoad}/>

<main>
	<h1>{name}</h1>
	<p>{@html desc}</p>
	{#if contents} <p>{contents}</p> {/if}
	{#if characters} <p>{characters}</p> {/if}
	<p> {#if exits.length > 0}
			You can go
		{/if}
		{#each exits as exit}
			<a on:click={() => handleClickExit(exit)}>{exit}</a><span>&nbsp;</span>
		{/each}
	</p>
</main>

<style>
	main {
		text-align: center;
		padding: 2em;
		margin: 0 auto;
		line-height: 1.5rem;
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
		margin-bottom: 2rem;
	}

	a {
		text-decoration: underline;
	}
	a:hover {
		cursor: pointer;
		color: rgb(255, 183, 183);
		text-decoration: underline;
	}
</style>
