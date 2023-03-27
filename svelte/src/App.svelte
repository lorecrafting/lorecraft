<script>
	let name;
	let desc;
	let contents = [];
	let characters = [];
	let exits = [];
	let msgToEvennia;
	let echoLogs = [];

	function handleWindowLoad() {
		Evennia.init()
		window.Evennia.emitter.on("room_data", function(empty, roomData) {
			name = roomData.name;
			desc = roomData.desc;
			contents = _formatContents(roomData.contents);
			characters = _formatCharacters(roomData.characters);
			exits = roomData.exits;
		})
		window.Evennia.emitter.on("text", function(text, cmd) {
			if (cmd.type === "look") {
				return
			}
			echoLogs = [...echoLogs, text[0]]
		})
	}

	function handleClickExit(exit) {
		Evennia.msg("text", [exit])
		echoLogs = [];
	}

	function onSubmit(e) {
		console.log(msgToEvennia)
		Evennia.msg("text", [msgToEvennia])
		msgToEvennia = '';
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
		let str;

		if (characters.length === 1) {
			return _upcaseFirstChar(`${characters[0]} is here.`)
		}
		if (characters.length === 2) {
			return _upcaseFirstChar(`${characters[0]} and ${characters[1]} are here.`)
		}
		if (characters.length > 2) {
			let lastChar = characters.pop();
			return _upcaseFirstChar(`${characters.join(", ")}, and ${lastChar} are here.`)
		}
	}

	function _upcaseFirstChar(str) {
		return str.charAt(0).toUpperCase() + str.slice(1);
	}
</script>

<svelte:window on:load={handleWindowLoad}/>

<main>
	<h1>{name}</h1>
	<p>{@html desc}</p>
	{#if contents}
		 <p>{contents}
			{#if characters}
				<span>{characters}</span>
			{/if}
		</p>
	{/if}

	<p> {#if exits.length > 0}
			You can go
		{/if}
		{#each exits as exit}
			<button on:click={() => handleClickExit(exit)}>{exit}</button><span>&nbsp;</span>
		{/each}
	</p>

	<br>

	<div>
		{#each echoLogs as exit}
			<p> {@html exit} </p>
		{/each}
	</div>


	<form on:submit|preventDefault={onSubmit}>
		<input bind:value={msgToEvennia} type="text">
	</form>
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

	button {
		text-decoration: underline;
		background-color: transparent;
		border-width: 0;
		font-family: inherit;
		font-size: inherit;
		font-style: inherit;
		font-weight: inherit;
		line-height: inherit;
		padding: 0;
	}
	button:hover {
		cursor: pointer;
		color: rgb(255, 183, 183);
		text-decoration: underline;
	}
</style>
