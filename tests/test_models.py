"""Tests for MEMOGEN data models."""

import pytest
from pydantic import ValidationError

from memogen.models import DifficultyLevel, UserProgress, VocabularyCard, VocabularyDeck


class TestVocabularyCard:
    """Tests for VocabularyCard model."""

    def test_create_valid_card(self, sample_easy_card: VocabularyCard) -> None:
        """Test creating a valid vocabulary card."""
        assert sample_easy_card.word == "ABUNDANT"
        assert sample_easy_card.level == DifficultyLevel.EASY
        assert sample_easy_card.ielts_band == "4-5"

    def test_card_validation_empty_word(self) -> None:
        """Test that empty word raises validation error."""
        with pytest.raises(ValidationError):
            VocabularyCard(
                word="",
                pronunciation="/test/",
                pos="noun",
                definition="test",
                example="test",
                synonyms="test",
                level=DifficultyLevel.EASY,
                ielts_band="4-5",
            )

    def test_card_default_emoji(self) -> None:
        """Test default emoji value."""
        card = VocabularyCard(
            word="TEST",
            pronunciation="/test/",
            pos="noun",
            definition="A test word",
            example="This is a test.",
            synonyms="exam, trial",
            level=DifficultyLevel.EASY,
            ielts_band="4-5",
        )
        assert card.emoji == "📚"


class TestVocabularyDeck:
    """Tests for VocabularyDeck model."""

    def test_create_empty_deck(self) -> None:
        """Test creating an empty vocabulary deck."""
        deck = VocabularyDeck(
            name="Test Deck",
            description="A test vocabulary deck",
        )
        assert deck.total_cards == 0
        assert len(deck.cards) == 0

    def test_deck_with_cards(
        self,
        sample_easy_card: VocabularyCard,
        sample_medium_card: VocabularyCard,
    ) -> None:
        """Test deck with multiple cards."""
        deck = VocabularyDeck(
            name="IELTS Deck",
            description="IELTS vocabulary",
            cards=[sample_easy_card, sample_medium_card],
        )
        assert deck.total_cards == 2

    def test_filter_by_level(
        self,
        sample_easy_card: VocabularyCard,
        sample_medium_card: VocabularyCard,
        sample_difficult_card: VocabularyCard,
    ) -> None:
        """Test filtering cards by difficulty level."""
        deck = VocabularyDeck(
            name="Mixed Deck",
            description="All levels",
            cards=[sample_easy_card, sample_medium_card, sample_difficult_card],
        )

        easy_cards = deck.filter_by_level(DifficultyLevel.EASY)
        assert len(easy_cards) == 1
        assert easy_cards[0].word == "ABUNDANT"

        medium_cards = deck.filter_by_level(DifficultyLevel.MEDIUM)
        assert len(medium_cards) == 1
        assert medium_cards[0].word == "AMBIGUOUS"


class TestUserProgress:
    """Tests for UserProgress model."""

    def test_create_new_user_progress(self) -> None:
        """Test creating new user progress."""
        progress = UserProgress(user_id="user123")
        assert progress.total_studied == 0
        assert progress.accuracy_rate == 0.0
        assert len(progress.learned_words) == 0

    def test_track_learned_words(self) -> None:
        """Test tracking learned words."""
        progress = UserProgress(user_id="user123")
        progress.learned_words.add("ABUNDANT")
        progress.learned_words.add("CAPTURE")

        assert len(progress.learned_words) == 2
        assert "ABUNDANT" in progress.learned_words

    def test_accuracy_validation(self) -> None:
        """Test accuracy rate validation."""
        with pytest.raises(ValidationError):
            UserProgress(
                user_id="user123",
                accuracy_rate=150.0,  # Invalid: > 100
            )

    def test_total_studied_validation(self) -> None:
        """Test total studied count validation."""
        with pytest.raises(ValidationError):
            UserProgress(
                user_id="user123",
                total_studied=-5,  # Invalid: negative
            )
