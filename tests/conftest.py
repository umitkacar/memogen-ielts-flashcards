"""Pytest configuration and fixtures."""

import pytest

from memogen.models import DifficultyLevel, VocabularyCard


@pytest.fixture
def sample_easy_card() -> VocabularyCard:
    """Create a sample easy-level vocabulary card."""
    return VocabularyCard(
        word="ABUNDANT",
        pronunciation="/əˈbʌndənt/",
        pos="adjective",
        definition="Available in large quantities; plentiful",
        example="The forest has abundant wildlife and natural resources.",
        synonyms="plentiful, copious, ample, profuse",
        level=DifficultyLevel.EASY,
        emoji="🌾",
        ielts_band="4-5",
    )


@pytest.fixture
def sample_medium_card() -> VocabularyCard:
    """Create a sample medium-level vocabulary card."""
    return VocabularyCard(
        word="AMBIGUOUS",
        pronunciation="/æmˈbɪɡjuəs/",
        pos="adjective",
        definition="Open to more than one interpretation; unclear or inexact",
        example="The politician's ambiguous statement left voters confused.",
        synonyms="unclear, vague, equivocal, cryptic",
        level=DifficultyLevel.MEDIUM,
        emoji="❓",
        ielts_band="6-7",
    )


@pytest.fixture
def sample_difficult_card() -> VocabularyCard:
    """Create a sample difficult-level vocabulary card."""
    return VocabularyCard(
        word="EPHEMERAL",
        pronunciation="/ɪˈfemərəl/",
        pos="adjective",
        definition="Lasting for a very short time; transitory",
        example="The beauty of cherry blossoms is ephemeral.",
        synonyms="fleeting, transient, momentary, brief",
        level=DifficultyLevel.DIFFICULT,
        emoji="🌸",
        ielts_band="8-9",
    )
